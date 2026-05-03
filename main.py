weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇



if bmi < 18.5:
    print("Your BMI is " + str(round(bmi, 2)) + ", you are underweight.")
elif bmi < 25:
    print("Your BMI is " + str(round(bmi, 2)) + ", you have a normal weight.")
else:
    print("Your BMI is " + str(round(bmi, 2)) + ", you are slightly overweight.")
