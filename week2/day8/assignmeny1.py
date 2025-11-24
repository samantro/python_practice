# week2/assignmeny1.py
# Write a function that takes a list of strings representing numerical data,
# cleans the data by removing any non-numeric entries, and converts the valid
# entries to integers. Use the map function to apply this cleaning function to
# the list.

from functools import reduce

def clean_data(data):
    if(not data.strip().isdigit()):
        return None
    return int(data.strip())


raw = [" 10", "20 ", "  abc", "55", "not available", "70 "]


cleaned_raw = list(map(clean_data, raw))

print("cleaned raw data of nums ", cleaned_raw)

# using dictionary comprehension

names = ["vishal", "RAHUL", " Priya "]

dict_names = {name.strip().title(): len(name.strip()) for name in names}
print("Dictionary names ", dict_names)


data = ["1", "2", "3", "4"]

map_lambda_data = list(map(lambda x: int(x), data))
print("map with lambda data ", map_lambda_data)

filtered_data = list(filter(lambda x: x is not None, cleaned_raw))
print("filtered cleaned data ", filtered_data)

data = [5, 10, 15, 20, 25]

result = reduce(lambda x, y: x + y, data)
print("reduced data sum ", result)