# working with text files in Python

print("Working with Files in Python")
with open('file_handling/example.txt', 'w') as file:
    file.write('Hello, This is day 6!\n')
    
with open('file_handling/example.txt', 'a') as file:
    file.write('Appending a new line to the file.\n')

with open('file_handling/example.txt', 'r') as file:
    content = file.read()
    print(content)


# working with csv files in Python

import csv

data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles']
]

print("Working with CSV Files in Python")
# write mode for csv file
with open('file_handling/example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# read mode for csv file
with open('file_handling/example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# working with json files in Python

import json

person = {
    'name': 'Charlie',  
    'age': 28,
    'city': 'Chicago' 
}

with open('file_handling/example.json', 'w') as file:
    json.dump(person, file, indent=2)

with open('file_handling/example.json', 'r') as file:
    data = json.load(file)
    print("Working with JSON Files in Python")
    print(data)