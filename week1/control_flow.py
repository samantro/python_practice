num=int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")  
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

for i in range(1,21):
    if i == 10:
        continue
    print(i, end=' ')
print()

num = 5
while num > 0:
    print(num, end=' ')
    num -= 1