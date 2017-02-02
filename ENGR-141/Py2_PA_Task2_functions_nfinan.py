# Activity 2.2.2: Python 2 PA Task 2 main
# File: Py2_PA_Task2_functions_nfinan.py
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
# functions used to do ideal gas calculations
import math

def pressure(t1,v,a,b,r):
    P = round((((r*t1)/(v-b)) - (a/(v**2))),2)
    return P
    
def required_temperature(P,t1,v,a,b,r):
    if P > 1.2:
        t2 = ((1.2 + (a / (v ** 2))) * (v - b)) / r
        return t2
    elif P < 1.1:
        t2 = ((1.1 + (a / (v ** 2))) * (v - b)) / r
        return t2
    else:
        t2 = t1
        return t2
def temperature_increment(t1,t2):
    tc = t2 - t1
    return tc
def new_pressure(t2,v,a,b,r):
    P2 = round((((r*t2)/(v-b)) - (a/(v**2))),2)
    return P2