print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')

#to get the above = ascii.art

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_one = input('You are at a crossroad, where do you want to go? Type "left" or "right".').lower()

if choice_one == "left":
    choice_two = input('You have come to the a lake. There is an island in the middle of the lake. '
          'Type "wait" to wait for the Boat. Type "swim" to swim across.').lower()
    if choice_two == "wait":
        choice_three = input('You have arrived unharmed at the island you are surrounded with 3 doors.'
              'One red, One yellow and One blue. Which color do you choose?').lower()
        if choice_three == "red":
            print("Its a room of Fire")
        elif choice_three == "yellow":
            print("You found the treasure. You Win!")
        elif choice_three == "blue":
            print("You entered a room of beasts. Game Over!")
        else:
            print("You choose the door that doesn't exist. Game Over!")
    else:
        print('You have been attached by Garwe, Game Over wangu!')

else:
    print("You fell into a hole, Game Over!!")

