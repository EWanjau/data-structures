#!/usr/bin/python3
"""Its a hangman game of guessing a letter
"""
# Step 1

import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
length = len(chosen_word)
print("The Chosen Word is: {}".format(chosen_word))

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ")
guess = guess.lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

display = []
for i in range(0, length):
    display.append("_")

for position in range(length):
    letter = chosen_word[position]
    if guess == letter:
        print("Correct!")
        display[position] = guess
    else:
        print("Incorrect")
print(display)
