# Py4 CFU
# File: Py4_CFU_nfinan.py
# Date: 7 October 2016
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
# finds summation and writes each sum to a txt file
target = float(input('Input the target value:'))
with open('myoutput.txt','w') as o:
    o.write('For a target value of', target)
    o.write('The Summation values at each interation are:')
    #close

k = 1
sum = 0
while sum <= target:
    sum += 1 / k
    k += 1
    with open('myoutput.txt','a') as o:
        o.writeline('%5.3f' %sum)
    #close