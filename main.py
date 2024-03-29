from dotenv import load_dotenv
import json
import ldclient
from ldclient import Config, ExecutionOrder, MigratorBuilder, Result, Stage
import logging
import os
import random
import sys
import time
from utils.create_context import create_multi_context
from utils.migration_functions import *

'''
Get environment variables
'''
load_dotenv()


'''
Set sdk_key and feature_flag_key to your LaunchDarkly environment, then initialize the LD client.
'''
SDK_KEY = os.environ.get('SDK_KEY')
FLAG_KEY = os.environ.get('FLAG_KEY')
ldclient.set_config(Config(SDK_KEY))

'''
Start logging!
'''
ld_logger = logging.getLogger("ldclient")
ld_logger.setLevel(logging.ERROR)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
ld_logger.addHandler(handler)


'''
Construct migrator builder
'''
builder = MigratorBuilder(ldclient.get())

# Define which two functions to call for read and writes, and how to check for consistency
builder.read(read_old(), read_new(), consistency_check())
builder.write(write_old(), write_new())

builder.read_execution_order(ExecutionOrder.PARALLEL)

default_stage = Stage.OFF
migrator = builder.build()


'''
Main loop to execute reads and writes
'''
while True:
    context = create_multi_context()

    # Out of 1000 reads, how many will fail
    read_error_rates = {
        "old": 30,
        "new": 11
        }

    # Out of 1000 writes, how many will fail
    write_error_rates = {
        "old": 20,
        "new": 10
        }

    read_result = migrator.read(FLAG_KEY, context, default_stage, read_error_rates)

    write_result = migrator.write(FLAG_KEY, context, default_stage, write_error_rates)

    time.sleep(10)