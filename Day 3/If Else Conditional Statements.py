# If / Else Conditional Statement

#Write some code that replaces the ticket box.
print("Welcome to the Roller Coaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you are not tall enough to ride the roller coaster.")

# Comparison Operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to  

# One '=' is an assignment operator, which is used to assign a value to a variable. (Assignment)
# Two '==' is a comparison operator, which is used to compare two values and returns True or False. (Check Equality between two values)

# Modulo Operator
# The modulo operator is represented by the symbol '%'. It returns the remainder of a division operation
# Example:
print(10 % 3) # Output: 1
print(15 % 4) # Output: 3
print(20 % 6) # Output: 2
print(10 % 5) # Output: 0

# Exercise: Odd or Even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:    print(f"{number} is an odd number.")   


