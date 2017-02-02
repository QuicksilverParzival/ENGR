# Activity Py1_PA: An introduction to Python.
# File: Py1_PA_Task2_nfinan.py
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
# Performs equivalent resistance for parallel and series system respectively. first resistance is user defined while second is predefined.
import math
r1 = float(input('Input the first resistance value:'))
r2 = math.sqrt(5.6) * math.pi
parallel = 1 / ((1 / r1) + (1 / r2))#parallel resistance
series = r1 + r2#series resistance
rr1 = round(r1,2)#rounded values
rr2 = round(r2,2)
rparallel = round(parallel,2)
rseries = round(series,2)
print('Type         First       Second          Equivalent Resistance')
print('Parallel    ',rr1,'ohms\t',rr2,'ohms\t',rparallel,'ohms')
print('Series      ',rr1,'ohms\t',rr2,'ohms\t',rseries,'ohms')