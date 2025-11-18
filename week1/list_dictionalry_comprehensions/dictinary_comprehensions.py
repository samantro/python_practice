# Dictionary comprehension to apply a 10% discount on item prices

prices = {
    'apple': 100,
    'banana': 60,   
    'orange': 120,
    'pear': 70
}

discounted_prices = {item: price * 0.9 for item, price in prices.items()}
print("discounted_prices: ", discounted_prices)

# nested comprehension to create a dictionary of squares
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for sublist in nested for num in sublist]
print("flat: ", flat)

# create dictionary from two lists using dictionary comprehension
items = ['apple', 'banana', 'orange', 'pear']
quantities = [5, 3, 8, 2]

inventory = {item: quantity for item, quantity in zip(items, quantities)}
print("inventory: ", inventory)

# nested dictionary comprehension to create a multiplication table

multiplication_table = {i: {j: i * j for j in range(1, 3)} for i in range(1, 6)}
print("multiplication_table: ", multiplication_table)


raw = ["   vishal", "  RAHUL  ", "  Anu  ", "  mohit  "]
cleaned = [name.strip().title() for name in raw]
print("cleaned: ", cleaned)