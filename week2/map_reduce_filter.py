# map, reduce, filter functions in Python

from functools import reduce
from typing import List, Callable
from operator import add

def map_function(func: Callable, data: List) -> List:
    """Applies a function to all items in the input list."""
    return list(map(func, data))  
def filter_function(func: Callable, data: List) -> List:
    """Filters items in the input list based on a function."""
    return list(filter(func, data)) 

def reduce_function(func: Callable, data: List, initial=None):
    """Reduces the input list to a single value using a binary function."""
    if initial is not None:
        return reduce(func, data, initial)
    return reduce(func, data)
# Example usage
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]

    # Map: Square each number
    squared = map_function(lambda x: x ** 2, data)
    print("Squared:", squared)

    # Filter: Keep only even numbers
    evens = filter_function(lambda x: x % 2 == 0, data)
    print("Evens:", evens)

    # Reduce: Sum all numbers
    total = reduce_function(add, data)
    print("Total:", total)