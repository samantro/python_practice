# traditional way

squares = []
for x in range(1, 10):
    squares.append(x**2)  
print(squares)


# list comprehension way

squares = [x**2 for x in range(1, 10)]
print(squares)

# consdensed way to create lists

even_squares = [x**2 for x in range(1, 10) if x % 2 == 0]
print(even_squares)