# This is a Tip Calculator

#Declarations
print("Welcome to Tip Calculator!")
total_bill = float(input("What was the total bill? R "))
tip = int(input("What percentage tip would you like to give? 10. 12, or 15 % "))
number_of_guest = int(input("How many people to split the bill? "))
bill_with_tip = round(tip / 100 * total_bill + total_bill,2)  # other maths => total_bill * (1 + tip / 100)
bill_per_person = round(bill_with_tip / number_of_guest,2)
# final_amount = round(bill_per_person, 2)
print(f"The Total bill is {bill_with_tip} Each person should pay R {bill_per_person} ")

