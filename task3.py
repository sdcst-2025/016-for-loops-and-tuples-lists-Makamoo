#! python3
"""
##### Task 3
Given a typle that contains a series of numbers, list all the ones that are
divisible by 5
(2 points)

inputs:
none

outputs:
list of numbers
25
10
30
75
20
"""

Pole = (25, 8, 10, 11, 33, 30, 51, 75, 63, 14, 20, 99)

for North in Pole:
    Snowman = float(North/5)
    Carrot = int(Snowman)
    Family = float(Carrot)
    if Snowman != Family:
        continue
    print(North)