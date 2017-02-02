# Python 3 CFU
# File: Py3_CFU_nfinan.py
# Date: 28 September 2016
# By: Nicholas Finan
# nfinan
# Section: 3
# Team: 38
#
# ELECTRONIC SIGNATURE
# Nicholas Finan
#
# The electronic signature above indicates that the program
# submitted for evaluation is my individual work. I have
# a general understanding of all aspects of its development
# and execution.
#
# provides coutdown and sum of candies crushed in all levels of a game
import math
n = int(input("Please enter the level completed most recently:"))
n = math.sqrt(n ** 2)
i = 1
o = n
sum = 0
print("The levels that have been completed are:")
while o >= 0:
    print(int(o))
    o = o - 1
while i <= n:
    sum += i
    i += 1
print("The total number of crushed candies is", sum,".")