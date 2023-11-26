#!/usr/bin/env python3
"""dictionary exercises are performed here
"""
import os
from art import logo_2

bidders = {}
max_bid = 0
is_bid = True
print(logo_2)
while (is_bid):
    prompt_choice = input("Do you Have  Bid?(yes/no)")
    if prompt_choice == "yes":
        os.system('clear')
        name = input("Please Enter Your Name: ")
        bid = int(input("Please enter Bid Amount: "))
        bidders[name] = bid
    else:
        for k, v in bidders.items():
            if max_bid < bidders[k]:
                max_bid = bidders[k]
        print("Maximum Bid Entered is: ".format(max_bid))
        is_bid = False
