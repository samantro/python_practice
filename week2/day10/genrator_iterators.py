# iterators in python
print("Iterators in Python:")

my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2   
print(next(my_iter))  # Output: 3
print(next(my_iter))  # Output: 4

# generator in python
print("\nGenerators in Python:")

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3


# Using a for loop with generator
print("\nUsing a for loop with generator:")

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1    

for number in count_up_to(5):
    print(number)  # Output: 1 2 3 4 5    

# Using generator expression
print("\nUsing generator expression:")

squares = (x * x for x in range(6))
gen = list(squares)
print(gen)  # Output: 0
print("after converting to list:", gen)  # Output: [0, 1, 4, 9, 16, 25]
for square in squares:
    print(square)  # Output: 0 1 4 9 16 25

# own iterator class

print("\nCustom Iterator Class:")

class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1
countdown = CountDown(5)
for number in countdown:
    print(number)  # Output: 5 4 3 2 1

# Practical example: Reading large file line by line using generator
print("\nReading large file line by line using generator:")
def read_large_file(path):
    with open(path, "r") as f:
        for line in f:
            yield line.strip()

for line in read_large_file("../week1/file_handling/example.txt"):
    print(line)