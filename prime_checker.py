#!/usr/bin/python3
"""Checks Prime No between a range of 0 - 100
Prime No is a number that is only divisible by itself and one
7 [ 1, 7]
8 [1, 2, 4, 8]
The algorithm is based on the fact that the no can only be modulus 0 with one and itself
2, 3, 5, 7, 11, 13, 17, 19, 23, 29
"""
print("The Module Checks for Prime Numbers between 0, 100 are:\n")


def prime_checker(number):
    prime_number = []
    divisibles = []

    if number > 7:
        prime_number = [2, 3, 5, 7]
        while (2 <= number):
            if number % 2 == 0 or number % 3 == 0:
                divisibles.append(number)
            elif number % 5 == 0 or number % 7 == 0:
                divisibles.append(number)
            else:
                prime_number.append(number)
            number -= 1
        prime_number.sort()
        print("Prime Numbers are:{}".format(prime_number))
    elif number == 7:
        prime_number.append(2)
        prime_number.append(3)
        prime_number.append(5)
        prime_number.append(7)
        print("Prime Numbers are:{}".format(prime_number))
    elif number >= 5:
        prime_number.append(2)
        prime_number.append(3)
        prime_number.append(5)
        print("Prime Numbers are:{}".format(prime_number))
    elif number >= 3:
        prime_number.append(2)
        prime_number.append(3)
        print("Prime Numbers are:{}".format(prime_number))
    elif number == 2:
        prime_number.append(number)
        print("Prime Numbers are:{}".format(prime_number))
    else:
        print("Invalid! Enter a Number Greater than 1")


n = int(input("Enter a Number:"))

prime_checker(number=n)
