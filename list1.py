#!/usr/bin/env python3
"""The module picks a random name from a list given and prints out a statement
"""
import random

names = ["Mike", "Tom", "John", "Walker",
         "Margaret", "Linet", "Kimani", "Anto"]

random_choice = random.randint(0, len(names) - 1)

print("{} is going to buy the meal today!".format(names[random_choice]))
