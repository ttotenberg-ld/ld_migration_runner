import names
import random
import uuid
from ldclient import Context
from faker import Faker

fake = Faker()

'''
Construct a user context
'''
def create_user_context():
  user_key = "usr-" + str(uuid.uuid4())
  name = f'{names.get_first_name()} {names.get_last_name()}'
  plan = random.choice(['platinum', 'silver', 'gold', 'diamond'])
  role = random.choice(['reader', 'writer', 'admin'])
  metro = random.choice(['New York', 'Chicago', 'Minneapolis', 'Atlanta', 'Los Angeles', 'San Francisco', 'Denver', 'Boston'])

  user_context = Context.builder(user_key) \
  .set("kind", "user") \
  .set("name", name) \
  .set("plan", plan) \
  .set("role", role) \
  .set("metro", metro) \
  .build()

  return user_context

'''
Construct a device context
'''
def create_device_context():
  device_key = "dvc-" + str(uuid.uuid4())
  os = random.choice(['Android', 'iOS', 'Mac OS', 'Windows'])
  version = random.choice(['1.0.2', '1.0.4', '1.0.7', '1.1.0', '1.1.5'])
  type = random.choice(['Fire TV', 'Roku', 'Hisense', 'Comcast', 'Verizon', 'Browser'])

  device_context = Context.builder(device_key) \
  .set("kind", "device") \
  .set("os", os) \
  .set("type", type) \
  .set("version", version) \
  .build()

  return device_context


'''
Construct an organization context
'''
def create_organization_context():
  org_key = "org-" + str(uuid.uuid4())
  # name = fake.company()
  key_name = random.choice([
    {"key": "org-7f9f58eb-c8e8-4c40-9962-43b13eeec4ea", "name": "Mayo Clinic"}, 
    {"key": "org-40fad050-3f91-49dc-8007-33d02f1869e0", "name": "IBM"}, 
    {"key": "org-fca878d0-3cab-4301-91da-bbc6dbb08fff", "name": "3M"}
    ])
  region = random.choice(['NA', 'CN', 'EU', 'IN', 'SA'])

  org_context = Context.builder(key_name["key"]) \
  .set("kind", "organization") \
  .set("name", key_name["name"]) \
  .set("region", region) \
  .build()

  return org_context

'''
Construct a multi context: User, Device, and Organization
'''
def create_multi_context():

  multi_context = Context.create_multi(
  create_user_context(),
  create_device_context(),
  create_organization_context()
  )

  return multi_context