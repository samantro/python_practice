# safe number convert

def safe_convert_to_float(value):
    try:
        return float(value.strip())
    except ValueError:
        return None

# Example usage
data = [" 3.14", " 2.71 ", " not a number ", " 42 ", " NaN "]
converted_data = list(map(safe_convert_to_float, data))
print("Converted data to float ", converted_data)  # Output: [3.14, 2.71, None, 42.0, nan]


# file handling with error handling, if file is not found  create a new file

def read_file_safe(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        with open(file_path, 'w') as file:
            file.write("This is a new file created because the original file was not found.")
        return f"File not found. A new file has been created at {file_path}."
    
# Example usage
print("Read existing file ", read_file_safe("../week1/file_handling/example.txt"))  # Should print file content if exists
print("Read non-existing file ", read_file_safe("new_file.txt"))  # Should create a new file and notify

def validate_score(score):
    if not (0 <= score <= 100):
        raise ValueError("Score must be between 0 and 100.")
    return score

# Example usage
try:
    print("Valid score ", validate_score(85))  # Output: 85
    print("Invalid score ", validate_score(150))  # This will raise ValueError
except ValueError as ve:
    print("Error:", ve)