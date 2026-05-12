
# For Loop
# loop allows to execute a line of code a multiple times

fruits = ['apple', 'Peach', 'Pear']
for fruit in fruits:
    print(fruit)
    print(fruit + ' Pie')
print(fruits) # this is outside the loops so after the inside code has run this will then run


# Mini Exercise
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)