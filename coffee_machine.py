#!/usr/bin/env python
""" This Module makes a coffee making machine
"""

# This function checks the user input
# while (True):
water = 300.0
milk = 300.0
coffee = 200.0
profit = 0.0
while profit >= 0.0:
    user_drink = input(
        "What Drink will you take Today?(espresso, latte, cappucinno)")
    match user_drink:
        case "espresso":
            if (water >= 30.0):
                if (milk >= 90.0):
                    if (coffee >= 6.0):
                        print("Ingredients are Sufficient")
                        quarters = float(input("Please Insert Quarters"))
                        dimes = float(input("Please Insert Dimes"))
                        nickles = float(input("Please Insert Nickles"))
                        penies = float(input("Please Insert Penies"))
                        total_cash = (quarters*0.25) + (dimes*0.10) + \
                            (nickles*0.05) + (penies*0.01)
                        if (total_cash >= 2.45):
                            print("Your Change is {:.2f}".format(
                                total_cash-2.45))
                            print("Enjoy Your Coffee")
                            profit += 2.45
                            water -= 30
                            milk -= 90
                            coffee -= 6
                        else:
                            print("Your Cash is not Sufficient")
                    else:
                        print("Sorry is not\
                            enough Coffee,Try again later")
                else:
                    print("Sorry is not enough Milk, Try again later")
            else:
                print("Sorry is not enough Water, Try again later")
        case "latte":
            if (water >= 200):
                if (milk >= 150):
                    if (coffee >= 100):
                        print("Ingredients are Sufficient")
                        quarters = float(input("Please Insert Quarters"))
                        dimes = float(input("Please Insert Dimes"))
                        nickles = float(input("Please Insert Nickles"))
                        penies = float(input("Please Insert Penies"))
                        total_cash = (quarters*0.25) + (dimes*0.10) + \
                            (nickles*0.05) + (penies*0.01)
                        if (total_cash >= 3.85):
                            print("Your Change is {:.2f}".format(
                                total_cash-3.85))
                            print("Enjoy Your Coffee")
                            profit += 3.85
                            water -= 200
                            milk -= 150
                            coffee -= 100

                        else:
                            print("Your Cash is not Sufficient")
                    else:
                        print("Sorry is\
                            not enough Coffee, Try again later")
                else:
                    print("Sorry is not enough Milk, Try again later")
            else:
                print("Sorry is not enough Water, Try again later")
        case "capuccinno":
            if (water >= 100):
                if (milk >= 85):
                    if (coffee >= 40):
                        print("Ingredients are Sufficient")
                        quarters = float(input("Please Insert Quarters"))
                        dimes = float(input("Please Insert Dimes"))
                        nickles = float(input("Please Insert Nickles"))
                        penies = float(input("Please Insert Penies"))
                        total_cash = (quarters*0.25) + (dimes*0.10) + \
                            (nickles*0.05) + (penies*0.01)
                        if (total_cash >= 3.15):
                            print("Your Change is {:.2f}".format(
                                total_cash-3.15))
                            print("Enjoy Your Coffee")
                            profit += 3.15
                            water -= 100
                            milk -= 85
                            coffee -= 40
                            Report = print("")
                        else:
                            print("Your Cash is not Sufficient")
                    else:
                        print("Sorry is\
                            not enough Coffee, Try again later")
                else:
                    print("Sorry is not enough Milk, Try again later")
            else:
                print("Sorry is not enough Water, Try again later")
        case "report":
            print("Water: {}".format(water))
            print("Milk: {}".format(milk))
            print("Coffee: {}".format(coffee))
            print("Money: {}".format(profit))
        case "off":
            exit()
        case _:
            print("Not Valid Input")
