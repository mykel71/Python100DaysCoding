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

#Nested If / Else Statements
# Example: Check if a number is positive, negative or zero
number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:    print(f"{number} is a negative number.")

#Continue:

print("Welcome to the Roller Coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print("Child Tickets are $5.")
    elif age <= 18:
        bill = 15
        print("Youth Tickets $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Would you like to see a photo? (y/n): ")
    if wants_photo == "y":
        # add $3 to their bill
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you are not tall enough to ride the roller coaster.")


#Pizza Delivery

print("Welcome to Python Pizza Delivery")
size = input("What size pizaa do you want? S, M, L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_chees = input("Do you want some extra cheese? Y or N: ")

## Small Pizza = $15, Medium = #20, Large = $25
## Add pepperoni to small pizza = $2
## Add pepperoni to medium and Large = $3
## Add extra cheese any size  = $1

# todo: work out how much they need to pay based on size and choice.
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid Inputs")

# todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
# todo: work out their final amount based on whether if they want extra cheese.
if extra_chees == "Y":
    bill += 1

print(f"Your final bill is ${bill}")


# Logical Operators

# AND, - Both conditions need to be true (True and True)
# OR, Only one condition needs to be true
# NOT, the condition must be false

