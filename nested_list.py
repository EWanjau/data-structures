#!/usr/bin/env python3
"""The Module Exercise is based on Knowledge of lists.
Combining two or more lists into one big list
"""
"""
    mark a spot on a map with an X
    variable = map(Nested List(3 lists in one))
    Write a Program that allows to mark a square on a map using Letter - No system
"""

# fruits = [12, 10, 20, 40]
# x = fruits.index(20)
# print(x)

# #         A    B    C
# line1 = ["⬜️", "️⬜️", "️⬜️"]
# line2 = ["⬜️", "⬜️", "️⬜️"]
# line3 = ["⬜️️", "⬜️️", "⬜️️"]

# map = [["A", "️B", "️C"], ["D", "️E", "️F"], ["G", "️H", "️I"]]
line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
if position[1] == '3':
    if position[0] == 'A':
        map[2][0] = "X"
    elif position[0] == 'B':
        map[2][1] = "X"
    else:
        map[2][2] = "X"
elif position[1] == '2':
    if position[0] == 'A':
        map[1][0] = "X"
    elif position[0] == 'B':
        map[1][1] = "X"
    else:
        map[1][2] = "X"
else:
    if position[0] == 'A':
        map[0][0] = "X"
    elif position[0] == 'B':
        map[0][1] = "X"
    else:
        map[0][2] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
