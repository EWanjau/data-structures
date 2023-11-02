#!/usr/bin/python3
"""Module checks calculates the can required for the paint
"""
import math


def paint_calc(height, width, cover):
    cans = math.ceil((height * width)/5)
    print("You'll need {} cans of paint.".format(cans))


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.
# 🚨 Don't change the code below 👇
test_h = int(input("Enter Height:\n"))  # Height of wall (m)
test_w = int(input("Enter Width: \n"))  # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
