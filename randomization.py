#!/usr/bin/python3
"""Randomization using lists and random module"""
import random


input("Enter a Number: ")
random_integer = random.randint(0, 1)
if random_integer == 0:
    print("Heads")
else:
    print("Tails")
