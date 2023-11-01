#!/usr/bin/python3
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
feedback = input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors")
comppick = random.randint(1, 3)
if feedback == 1:
    print("You chose: {}".rock)
    if comppick == 2:
        print("Computer Chose:{}".paper)
        print('You Lose')
    elif comppick == 3:
        print("Computer Chose:{}".scissors)
        print('You Win')
elif feedback == 2:
    print("You chose: {}".paper)
    if comppick == 1:
        print("Computer Chose:{}".rock)
        print('You Win')
    elif comppick == 3:
        print("Computer Chose:{}".scissors)
        print('You Lose')
else:
    print("You chose: {}".scissors)
    if comppick == 1:
        print("Computer Chose:{}".rock)
        print('You Lose')
    elif comppick == 2:
        print("Computer Chose:{}".paper)
        print('You Win')
