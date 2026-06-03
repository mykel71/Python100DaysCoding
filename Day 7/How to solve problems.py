# Flow chart programming is a way to plan out your code before you write it. It helps you to think about the logic of your program and how different parts of your code will interact with each other.

# For example a Hangman Game
# 1. Start the game
# 2. Choose a random word
# 3. Display the word with blanks for each letter
# 4. Ask the user to guess a letter
# 5. If the letter is in the word, fill in the blanks with the letter
# 6. If the letter is not in the word, add a body part to the hangman
# 7. Repeat steps 4-6 until the user guesses the word or the hangman is complete
# 8. End the game

import random


word_list = ["ardvark", "baboon", "camel"]
print(word_list)

#To do 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
secret_word = random.choice(word_list)

# to do 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
print(guess)

# to do 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. If it is, print "Right". Otherwise, print "Wrong".
for letter in secret_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
