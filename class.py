import json

# Load the JSON data from the file
file_path = 'filtered_user_names.json'
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Categories based on the given rules
categories = {
    "numbers": [],
    "keywords": [],
    "single_word": [],
    "patronymic": [],
    "symbols": []
}

# Helper functions to classify nicknames
def is_numbers(nickname):
    return any(char.isdigit() for char in nickname)

def is_keywords(nickname):
    # Define a simple check for keywords (extendable)
    keywords = ["pro", "gamer", "master", "love", "boss"]
    return any(keyword.lower() in nickname.lower() for keyword in keywords)

def is_single_word(nickname):
    return len(nickname.split()) == 1

def is_patronymic(nickname):
    return nickname.lower().endswith(("ovich", "evich", "ovna", "ich"))

def is_symbols(nickname):
    return any(not char.isalnum() and not char.isspace() for char in nickname)

# Process each nickname and categorize it
for user in data:
    nickname = user.get("nickname", "").strip()
    if not nickname:
        continue
    if is_numbers(nickname):
        categories["numbers"].append(nickname)
    elif is_keywords(nickname):
        categories["keywords"].append(nickname)
    elif is_patronymic(nickname):
        categories["patronymic"].append(nickname)
    elif is_symbols(nickname):
        categories["symbols"].append(nickname)
    elif is_single_word(nickname):
        categories["single_word"].append(nickname)
    

# Save the categorized nicknames into a JSON file
output_path = 'categorized_nicknames.json'

with open(output_path, 'w', encoding='utf-8') as output_file:
    json.dump(categories, output_file, ensure_ascii=False, indent=4)

output_path