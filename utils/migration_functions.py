from ldclient import Result
import json
import random
import time
from dotenv import load_dotenv


def write_new():
    def randomizer(error_rate):
        new_rate = error_rate['new']
        value = random.randint(1, 1000)
        # Intentional pause to simulate write latency
        time.sleep(.2)
        if value >= new_rate:
            print("NEW WRITE: SUCCESS")
            return Result.success("WRITE: SUCCESS")
        else:
            print("NEW WRITE: FAIL")
            return Result.fail("WRITE: FAIL")
    return randomizer

def write_old():
    def randomizer(error_rate):
        old_rate = error_rate['old']
        value = random.randint(1, 1000)
        # Intentional pause to simulate write latency
        time.sleep(.35)
        if value >= old_rate:
            print("OLD WRITE: SUCCESS")
            return Result.success("WRITE: SUCCESS")
        else:
            print("OLD WRITE: FAIL")
            return Result.fail("WRITE: FAIL")
    return randomizer

def read_new():
    def randomizer(error_rate):
        new_rate = error_rate['new']
        value = random.randint(1, 1000)
        # Intentional pause to simulate read latency
        time.sleep(.2)
        if value >= new_rate:
            # Add an additional check on succesful read to determine whether this will be consistent with the other read
            consistency_value = random.randint(1, 1000)
            if consistency_value <= 998:
                print("NEW READ: CONSISTENT")
                return Result.success("READ: CONSISTENT")
            else: 
                print("NEW READ: INCONSISTENT")
                return Result.success("READ: INCONSISTENT")
        else:
            print("NEW READ: FAIL")
            return Result.fail("READ: FAIL")
    return randomizer

def read_old():
    def randomizer(error_rate):
        old_rate = error_rate['old']
        value = random.randint(1, 1000)
        # Intentional pause to simulate read latency
        time.sleep(.4)
        if value >= old_rate:
            # Add an additional check on succesful read to determine whether this will be consistent with the other read
            consistency_value = random.randint(1, 1000)
            if consistency_value <= 998:
                print("OLD READ: CONSISTENT")
                return Result.success("READ: CONSISTENT")
            else: 
                print("OLD READ: INCONSISTENT")
                return Result.success("READ: INCONSISTENT")
        else:
            print("OLD READ: FAIL")
            return Result.fail("READ: FAIL")
    return randomizer

def consistency_check():
    def check_consistency(a, b):
        if a == b:
            print("Consistency: TRUE")
            return True
        else:
            print("Consistency: FALSE")
            return False
    return check_consistency
