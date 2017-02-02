# Question 18
# File: filename.py
# Date: 3 October 2016
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
# checks to see if the function semiCurrent is running properly

def semiCurrent(V):
    if 20 > V > 10:
        C = 10 - V
        return C
    elif 0 < V < 10:
        C = 10.0
        return C
	
    else:
        C = -999
        return C
		
V = float(input("Please enter the voltage (in V):"))
C = semiCurrent(V)
if C != -999:
    print("The corresponding current is", C,"A")
else:
    print("The current is undefined")