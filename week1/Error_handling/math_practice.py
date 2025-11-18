from math import sqrt, ceil, floor, pow
import helper

def safe_sqrt(value):
    """Returns the square root of a number if non-negative, else raises ValueError."""
    if value < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return sqrt(value)

def ceil_and_floor(value):
    """Returns a tuple containing the ceiling and floor of the given value."""
    return (ceil(value), floor(value))

def power(base, exponent):
    """Returns the result of raising base to the power of exponent."""
    return pow(base, exponent)  

# Example usage:
if __name__ == "__main__":      
    try:
        print("Square root of 16:", safe_sqrt(16))
        print("Ceiling and Floor of 4.7:", ceil_and_floor(4.7))
        print("2 raised to the power of 3:", power(2, 3))
        print("Square root of -4:", safe_sqrt(-4))  # This will raise an error

    except ValueError as e:
        print("Error:", e)  

    try:
        print("Cleaned name:", helper.clean_name("  vishal  "))
        print("Safe int conversion of '42':", helper.safe_int("42"))
        print("Safe int conversion of 'abc':", helper.safe_int("abc"))  # This will raise an error
    except (TypeError, ValueError) as e:
        print("Error:", e)