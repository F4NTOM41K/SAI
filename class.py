import json

# Load the JSON data from the file
file_path = 'filtered_user_names.json'
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Categories based on the given rules
categories = {
    "frenonim": [],
    "titlonim": [],
    "etnonim": [],
    "incognitonim": []
}

# Helper functions to classify nicknames
def is_frenonim(nickname):
    return nickname

def is_titlonim(nickname):
    # Define a simple check for keywords (extendable)
    keywords = ["pro", "gamer", "master", "love", "boss", "night"]
    return any(keyword.lower() in nickname.lower() for keyword in keywords)

def is_etnonim(nickname):
    return len(nickname.split()) == 1

def is_incognitonim(nickname):
    return nickname.lower().endswith(("ovich", "evich", "ovna", "ich"))


# Process each nickname and categorize it
count = 0
for user in data:
    nickname = user.get("nickname", "").strip()
    if not nickname:
        continue
    if is_frenonim(nickname):
        categories["frenonim"].append(nickname)
        count+=1
    elif is_titlonim(nickname):
        categories["titlonim"].append(nickname)
        count+=1
    elif is_etnonim(nickname):
        categories["etnonim"].append(nickname)
        count+=1
    elif is_incognitonim(nickname):
        categories["incognitonim"].append(nickname)
        count+=1


# Save the categorized nicknames into a JSON file
output_path = 'categorized_nicknames.json'

with open(output_path, 'w', encoding='utf-8') as output_file:
    json.dump(categories, output_file, ensure_ascii=False, indent=4)

print(count)