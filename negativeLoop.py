# ask for user input to enter a number everytime until the user enters a negative number

# Prompt the user to enter a negative number
number = int(input("Enter a negative number:"))

# Keep asking until a negative number is entered
while number >= 0:  # Loop continues if the number is not negative
    print("That's not a negative number!")
    number = int(input("Enter a negative number:"))

# Exit message
print("You entered a negative number. Program ends.")

        
        
        