# Python 1 ACT: Introduction to Python
# File: Py1_ACT_Task1_mccaul.py
# Date: 14 September 2016
# By: Alessandro Brown
# brow1359
# Nicholas Finan
# nfinan
# Andrew McCaul
# mccaul
# Josiah Rudge
# jrudge
# Section: 3
# Team: 38
#
# ELECTRONIC SIGNATURE
# Alessandro Brown
# Nicholas Finan
# Andrew McCaul
# Josiah Rudge
#
# The electronic signatures above indicate that the program
# submitted for evaluation is the combined effort of all
# team members and that each member of the team was an
# equal participant in its creation. In addition, each
# member of the team has a general understanding of
# all aspects of the program development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE PROGRAM OR FUNCTION DOES 
# The program computes the area of a triangle with two side 
# lengths being 12 cm and 4 cm and the angle between them
# being 30 degrees. It uses the formula Area = (1/2) * a * b * sin(C) 
# (C being in radians) to find a result.

# Area of Triangle

import math
a = 12
b = 4
C = 30
C = math.pi / 6 # convert C from degrees to radians for clarity
Area = (1/2) * a * b * math.sin(C)
math.ceil(Area)
print('The area of the triangle is', math.ceil(Area))