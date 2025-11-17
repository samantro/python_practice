raw = [
    {"name": " vishal ", "age": " 25", "city": "delhi "},
    {"name": "  RAHUL", "age": "not known", "city": " mumbai"},
    {"name": "priya ", "age": " 30 ", "city": " pune"}
]

def clean_data(data):
    cleaned = []
    for entry in data:
        name = entry['name'].strip().title()
        city = entry['city'].strip().title()
        age_str = entry['age'].strip()
        if age_str.isdigit():
            age = int(age_str)
        else:
            age = None
        cleaned.append({'name': name, 'age': age, 'city': city})
    return cleaned
cleaned_data = clean_data(raw)

import csv, json


# Write cleaned data to CSV and JSON files

with open('file_handling/cleaned.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_data)

with open('file_handling/cleaned.json', 'w') as jsonfile:
    json.dump(cleaned_data, jsonfile, indent=2)

# Read back the data from CSV and JSON files to verify

with open('file_handling/cleaned.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    print("Data read from cleaned.csv:")
    for row in reader:
        print(row)

with open('file_handling/cleaned.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    print("Data read from cleaned.json:")
    print(data)