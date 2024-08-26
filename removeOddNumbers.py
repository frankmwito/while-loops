# remove odd numbers from a list

num = int(input("Enter any number for size of list:"))
numbers = list()

for i in range(num):
    numbers.append(int(input("Enter any number:")))
    
print(numbers)

i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        numbers.pop(i)
    else:
        i += 1
        
print(numbers)