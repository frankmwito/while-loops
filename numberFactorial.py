# calculate the factorial of a number

number = int(input("Enter any number:"))
factorial = 1
i = 1

while i <= number:
    factorial *= i
    i += 1
    
print(factorial)