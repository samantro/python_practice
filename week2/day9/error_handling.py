# basic try-except example
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    else:
        return result
# Example usage
print("Divide with 2", divide_numbers(10, 2))  # Output: 5.0
print("Divide with zero ", divide_numbers(10, 0))  # Output: Error: Cannot divide by


# invalid typeprint("Divide with string ", divide_numbers(10, "a"))  # Output: Error: Invalid input type. Please provide numbers.

print("Divide with string ", divide_numbers(10, "a"))  # Output: Error: Invalid input type. Please provide numbers.


def open_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        return f"Error: The file at {file_path} was not found."
    except IOError:
        return f"Error: An I/O error occurred while trying to read the file at {file_path}."
    else:
        return content
  
# Example usage
print("Open existing file ", open_file("../week1/file_handling/example.txt"))  # Should print file content
print("Open non-existing file ", open_file("non_existing_file.txt"))  # Output: Error: The file at non_existing_file.txt was not found.

# custom error example

def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return number ** 0.5  

# Example usage
try:
    print("Square root of 16 is ", calculate_square_root(16))  # Output: 4.0
    print("Square root of -4 is ", calculate_square_root(-4))  # This will raise ValueError 
except ValueError as ve:
    print("Error:", ve)


# handling error with finally

def read_file(file_path):
    try:
        file = open(file_path, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file at {file_path} was not found."
    finally:
        try:
            file.close()
        except UnboundLocalError:
            pass  # file was never opened

# Example usage
print("Read existing file ", read_file("../week1/file_handling/example.txt"))  # Should print file content
print("Read non-existing file ", read_file("non_existing_file.txt"))  # Output: Error: The file at non_existing_file.txt was not found.