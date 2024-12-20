#Task 5
"""
Iterate through the list of numbers.
If the number is positive, determine the square root of the number.
State the number and the square root value
"""
import math

Bells = (5,-2,12,-8,14,16)

for Jingle in Bells:
    if Jingle <= 0:
        continue
    else:
        Tree = math.sqrt(Jingle)
        print(f"The square root of {Jingle} is {Tree}")