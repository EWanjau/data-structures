#!/usr/bin/python3
"""This module calculates the average heights of a list of inputs
"""
student_heights = input(
    "Enter a List of Heights separated by a space:").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
sum = 0
count = 0
high_score = 0
for mark in student_heights:
    count += 1
    sum += mark
    if mark > high_score:
        high_score = mark

average = round(sum / count)

print("total height = {}".format(sum))
print("number of students = {}".format(count))
print("average height = {}".format(average))
print("The highest score in the class is: {}".format(high_score))
