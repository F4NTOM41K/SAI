import json
import random

# Load the JSON data from the file
file_path = 'categorized_nicknames.json'
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Flatten all categories into a single list
all_records = []
for category in data.values():
    all_records.extend(category)

# Shuffle and split the data into 80:20 ratio
random.shuffle(all_records)
split_point = int(len(all_records) * 0.8)
train_set = all_records[:split_point]
test_set = all_records[split_point:]

# Save the split datasets back to JSON
output_data = {
    "train_set": train_set,
    "test_set": test_set
}

# Save train and test datasets into separate files
train_file_path = 'train_categorized_nicknames.json'
test_file_path = 'test_categorized_nicknames.json'

with open(train_file_path, 'w', encoding='utf-8') as train_file:
    json.dump({"train_set": train_set}, train_file, ensure_ascii=False, indent=4)

with open(test_file_path, 'w', encoding='utf-8') as test_file:
    json.dump({"test_set": test_set}, test_file, ensure_ascii=False, indent=4)

train_file_path, test_file_path

