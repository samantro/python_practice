from functools import reduce

nums = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, nums)
print(total)  # Output: 15

squared = list(map(lambda x: x ** 2, nums))
print(squared)  # Output: [1, 4, 9, 16, 25]

even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # Output: [2, 4]