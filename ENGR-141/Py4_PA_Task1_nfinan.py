# Python 4 PA Task 1
# File: Py4_PA_Task1_nfinan.py
# Date: 13 October 2016
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
# Reads and numbers steps from selected file. Output results to a file of user's choice.
inputFile = input('Enter the filename of the input file:')
outputFile = input('Enter the filename of the output file:')
inp = open(inputFile , 'r')
out = open(outputFile , 'w')
list = inp.readlines()
for var in list:
    if list.index(var) != list.index(list[-1]):
        var2 = var[:-1]
        line = ('Step ' + str((list.index(var) + 1)) + ': ' + var2)
        out.write(line)
        out.write('\r\n')
    else:
        line = ('Step ' + str((list.index(var) + 1)) + ': ' + var)
        out.write(line)
        out.write('\r\n')


inp.close()
out.close()