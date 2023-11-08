#!/usr/bin/python3
"""This Module Plays a simple game of Random Choices
"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Write your code below this line 👇
game_choice = [rock, paper, scissors]
feedback = int(input("Enter 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))
if feedback >= 3 or feedback < 0:
    print("You have entered an Invalid Number")
else:
    print("You chose {}".format(game_choice[feedback]))
    comppick = random.randint(0, 2)
    print("Computer chose {}".format(game_choice[comppick]))

    if feedback == 0:
        if comppick == 1:
            print('You Lose')
        elif comppick == 2:
            print('You Win')
        else:
            print("Repeat")
    elif feedback == 1:
        if comppick == 0:
            print('You Win')
        elif comppick == 2:
            print('You Lose')
        else:
            print("Repeat")
    else:
        if comppick == 0:
            print('You Lose')
        elif comppick == 1:
            print('You Win')
        else:
            print("You Draw")
