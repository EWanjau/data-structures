#!/usr/bin/python3
"""the module generates a radom password which the user specifies
"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to my Py Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

formed_letter = ""
for letter in range(0, (nr_letters)):
    formed_letter += random.choice(letters)
    formed_symbol = ""
    for symbol in range(0, (nr_symbols)):
        formed_symbol += random.choice(symbols)
    formed_number = ""
    for number in range(0, (nr_numbers)):
        formed_number += random.choice(numbers)

password = formed_letter + formed_symbol + formed_number
shuffled_pass = list(password)
random.shuffle(shuffled_pass)
result = ''.join(shuffled_pass)
print("Your Password is:\n{}".format(result))
