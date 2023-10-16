#!/usr/bin/python3
"""The module calculates teh factorial of a no entered by the user
"""


def factorial(a):
    i = int(a)
    fact = 0
    while int(i) > 0:
        fact = fact + a * (i - 1)
        --i
        --a
    return print("The Factorial is: {:2}".fact)


while True:
    number = input("Enter a Positive Number : ")
    if int(number) < 0:
        print("Invalid No. Enter a Positive Integer")
    else:
        factorial(number)
