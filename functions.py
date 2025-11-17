def greet(name):
    print("Hello {0}, Welcome to Python!".format(name))

greet("Vishal")

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(5))


def add_numbers(*numbers):
    return sum(numbers)

print(add_numbers(1, 2, 3, 4, 5))

def multiply(a, b=2):
    return a * b

print(multiply(5))
print(multiply(5, 3))