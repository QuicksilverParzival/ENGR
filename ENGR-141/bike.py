# Activity X.X.X: An introduction to Python.
# File: filename.py
# Date: 1 September 2016
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

import csv
import math

file = str(input('Input csv file name: '))

#initial values for for loop
sum_x = 0
sum_x2 = 0
sum_y = 0
sum_xy = 0
sum_lny = 0
sum_lnx = 0
sum_lnyx = 0
sum_lnx2 = 0
sum_lnylnx = 0
numLines = 0

SST = 0

with open(file, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    for row in spamreader:
        numt = ','.join(row)
        num = numt.split(',')
        #print(float(num[1]))
        #print(type(float(num[1])))
        
        sum_x += float(num[0])
        sum_x2 += (float(num[0]) ** 2)
        sum_y += float(num[1])
        sum_xy += (float(num[0]) * float(num[1]))
        sum_lny += math.log(float(num[1]))
        sum_lnx += math.log(float(num[0]))
        sum_lnx2 += math.log(float(num[0])) ** 2
        sum_lnyx += (math.log(float(num[1])) * float(num[0]))
        sum_lnylnx += (math.log(float(num[0])) * math.log(float(num[1])))
        numLines += 1

#Calculate SST
with open(file, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    for row in spamreader:
        numt = ','.join(row)
        num = numt.split(',')
        SST += (((sum_y / numLines) - float(num[1])) ** 2)
    print('SST', SST) 

#Linear Model
a0lin = ((sum_y * sum_x2) - (sum_x * sum_xy)) / ((numLines * sum_x2) - (sum_x * sum_x))
a1lin = ((numLines * sum_xy) - (sum_y * sum_x)) / ((numLines * sum_x2) - (sum_x * sum_x))
print('a0lin', a0lin)
print('a1lin', a1lin)

#Calculate SSE for linear model
SSE = 0
with open(file, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    for row in spamreader:
        numt = ','.join(row)
        num = numt.split(',')
        SSE += ((a0lin + (a1lin * float(num[0]))) - float(num[1])) ** 2

    r2_lin = 1 - (SSE / SST)
    print('R^2 Linear', r2_lin)

#Exponential Model
a0exp = math.exp(((sum_lny * sum_x2) - (sum_x * sum_lnyx)) / (sum_x2 - (sum_x * sum_x)))
a1exp = ((numLines * sum_lnyx) - (sum_lny * sum_x)) / ((numLines * sum_x2) - (sum_x * sum_x))

#Calculate SSE for exponential model
SSE = 0
with open(file, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    for row in spamreader:
        numt = ','.join(row)
        num = numt.split(',')
        SSE += ((a0exp * math.exp(a1exp * float(num[0]))) - float(num[1])) ** 2

    r2_exp = 1 - (SSE / SST)
    print('R^2 Exponential', r2_exp)

#Power model
a0pow = math.exp(((sum_lny * sum_lnx2) - (sum_lnx * sum_lnylnx)) / (sum_lnx2 - (sum_lnx * sum_lnx)))
a1pow = ((numLines * sum_lnylnx) - (sum_lny * sum_lnx)) / ((numLines * sum_lnx2) - (sum_lnx * sum_lnx))

#Calculate SSE for power model
SSE = 0
with open(file, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    for row in spamreader:
        numt = ','.join(row)
        num = numt.split(',')
        SSE +=  ((a0pow *(float(num[0]) ** a1pow)) - float(num[1])) ** 2

    r2_pow = 1 - (SSE / SST)
    print('R^2 Power', r2_pow)

#Chooses which model to use from the highest r^2 value
if r2_lin > r2_exp:
    if r2_lin > r2_pow:
        print('Linear model to be used')
        a0 = a0lin
        a1 = a1lin
    else:
        print('Power model to be used')
        a0 = a0pow
        a1 = a1pow
if r2_exp > r2_lin:
    if r2_exp > r2_pow:
        print('Exponential model to be used')
        a0 = a0exp
        a1 = a1exp
print('a0 value for model:', a0)
print('a1 value for model:', a1)
print('a0 value for exp:', a0exp)
print('a1 value for exp:', a1exp)