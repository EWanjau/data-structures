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
feedback = input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors:")
comppick = random.randint(1, 3)

if feedback == '1':
    print("You chose: {}".format(rock))
    if comppick == 2:
        print("Computer Chose:{}".format(paper))
        print('You Lose')
    elif comppick == 3:
        print("Computer Chose:{}".format(scissors))
        print('You Win')
    else:
        print("Computer Chose:{}".format(rock))
        print("Repeat")
elif feedback == '2':
    print("You chose: {}".format(paper))
    if comppick == 1:
        print("Computer Chose:{}".format(rock))
        print('You Win')
    elif comppick == 3:
        print("Computer Chose:{}".format(scissors))
        print('You Lose')
    else:
        print("Computer Chose:{}".format(paper))
        print("Repeat")
elif feedback == '3':
    print("You chose: {}".format(scissors))
    if comppick == 1:
        print("Computer Chose:{}".format(rock))
        print('You Lose')
    elif comppick == 2:
        print("Computer Chose:{}".format(paper))
        print('You Win')
    else:
        print("Computer Chose:{}".format(scissors))
        print("Repeat")
else:
    print("Sorry, Enter A Valid Option")
