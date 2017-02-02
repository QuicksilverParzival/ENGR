# Activity Py1_PA: An introduction to Python.
# File: Py1_PA_Task1_nfinan.py
# Date: 21 September 2016
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
# Randomly generates integers and displays addition in decimal and fraction form.
import random
from fractions import Fraction
random.seed(1)
a = round(10*random.random(),1)
af = round(Fraction(a),1)
random.seed(2)
b = round(10*random.random(),1)
bf = round(Fraction(b),1)
random.seed(1)
print("First Random Number:",10*random.random())
random.seed(2)
print("Second Random Number:",10*random.random())
print(a," + ", b," = ", round(a+b,1))
print(af," + ", bf," = ", round(Fraction(round(a+b,1)),1))