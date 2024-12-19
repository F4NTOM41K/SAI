from bson import decode_all
import random
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the users.bson file
bson_file_path = os.path.join(script_dir, 'VDatabase\vkData\walls.bson')

# Read the BSON data from the file
with open(bson_file_path, 'rb') as f:
    users_data = f.read()

# Decode the BSON data
users = decode_all(users_data)

# Get a random user
random_user = random.choice(users)

print("Random User:", random_user)