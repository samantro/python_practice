name="Vishal Verma"
age=25
city="New Delhi"

print(f"My name is {name}, I am {age} years old, I live in {city}")
print(type(name))


num1, num2 = 10, 20
sum = num1 + num2
difference = num2 - num1
power = num1 ** num2
floor_division = num2 // num1

print("The sum of {0} and {1} is {2}".format(num1, num2, sum))
print("The difference when {1} is subtracted from {0} is {2}".format(num2, num1, difference))
print("The value of {0} raised to the power {1} is {2}".format(num1, num2, power))
print("The floor division of {0} by {1} is {2}".format(num2, num1, floor_division))