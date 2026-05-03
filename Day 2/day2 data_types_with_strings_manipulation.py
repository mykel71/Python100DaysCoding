#Python Primitive Data Type
import pr

#String
print("Michael"[-1]) # -1 means get the last character


#Integers = Whole Numbers
print(123 + 345)
print(123_345_456) # this is still an integer in py


#Float
print(3,412)

#Booleans
print(True)
print(False)

#Data Types & Functions

len("12345") # len func only deals with string


# to check the data type
# noinspection PyStringConversionWithoutDunderMethod
print(type('Hello Fam'))
print(type(123))
print(type(123.456))
print(type(True))

# Data Casting

print("123" + "345")
print(int(123) + int(345)) # here its nolonger a string but an integer

#However you need to be careful given you can't convert "abc" to an integer

# Fix this problem
# print("number of letter in your name: " + len("Enter your name")) # fix this

#Solution
name_of_the_user = input("Enter your name: ") # type string
length = len(name_of_the_user) #type int
print("Number of letters in your name: " + str(length))


print("My age is: " + str(32))

#Mathematical Operations
# Lear to use the basic mathematical operators , +,-,*,/ and ''

#PEMDAS(LR)
#Parentheses, Exponents, Multiplication/Division, Addition/Subtration
print(123 + 456)
print(7-3)
print(3 * 2)
print(6 / 3)
print(3 // 2)
print(3 % 2)
print(3 ** 2)


# Be aware when you have many calculation on the same line - Just like BOMDAS here its #PEMDAS(LR) LR means L to R
# #Parentheses, Exponents, Multiplication/Division, Addition/Subtration - This should be the order

## e.g NB - The order matters: What is the order
print(3 * 3 + 3 / 3 - 3)
# change this to give you 3 not 7
print(3 * (3 + 3 )/ 3 - 3) # just add parentheses


#Exercise

###BMI Calculator
#The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:
#bmi is equal to the person's weight divided by the person's height squared.
#Convert this sentence into code on line 6.

height = 1.65
weight = 84

# Calculate the bmi using weight and height.
bmi = weight / (height * height) # another way of doing it  = (bmi = 84 / 1.65 ** 2)

print(bmi)


# Number Manipulation & F-String
print(int(bmi)) # converts to int

print(round(bmi)) # rounding of to the nearest
print(round(bmi, 2)) # rounding of to the nearest but decimal

# Assignment operators
score = 0

#user scores a point
score += 1
print(score)

# F- String - The ability to mix strings and data types
print("Your score is " + str(score)) # The old way
#The new Way
print(f"Your score is {score}.")

# Another example:

score = 0
height = 1.8
is_winning = True

print(f"Your score is {score}, Your Height is {height} and your is_winning is {is_winning}")


