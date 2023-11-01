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
    random_letter = random.randint(0, len(letters)-1)
    formed_letter += letters[random_letter]
    formed_symbol = ""
    for symbol in range(0, (nr_symbols)):
        random_symbol = random.randint(0, len(symbols)-1)
        formed_symbol += symbols[random_symbol]
    formed_number = ""
    for number in range(0, (nr_numbers)):
        random_number = random.randint(0, len(numbers)-1)
        formed_number += numbers[random_number]
password = formed_letter + formed_symbol + formed_number
shuffled_pass = list(password)
random.shuffle(shuffled_pass)
result = ''.join(shuffled_pass)
print("Your Password is:\n{}".format(result))
