# Python Post Activity 3
# File: Py3_PA_Task1_nfinan.py
# Date: 4 October 2016
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
# Can find derivatives of defined function if given a limit of accuracy and an initial guess

coef = input('Enter coefficents:').split()
coef.reverse()
goal = float(input('Enter goal value:'))
guess = float(input('Enter initial guess:'))
tolerance = float(input('Enter a tolerance:'))
maxIter = float(input('Enter maximum allowable iterations:'))

def findOrder(coef):
    if coef[0] == 0:
        order = len(coef) - 1
    else:
        order = len(coef)
        
    return order


def funcVal(coef, x):
    func = 0
    i = 0
    for val in coef:
        y = float(val)
        term = y * (x ** i)
        func += term
        i += 1
    return func

def derVal(coef, x):
    i = 0
    derivative = 0
    for val in coef:
        y = float(val)
        dterm = i * y * (x ** (i - 1))
        derivative += dterm
        i += 1
    return derivative
iter = 1
val = 0.0
print('The polynomial entered is of order:', findOrder(coef))
while val <= tolerance:
    if iter >= maxIter:
        print('Program Terminated, Maximum iterations exceeded.')
    else:
        val = guess - (funcVal(coef, guess) / derVal(coef, guess))
        print(iter, ': x =' , val, ', f(x) =', funcVal(coef, guess))
        guess = val
        iter += 1

print('A solution was estimated to be:', val)
print('Total number of iterations:', iter - 1)