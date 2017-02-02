# Exam 2 Question 17
# File: exam2_q17_nfinan.py
# Date: 11 November 2016
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
# Calculates days including leap years
year1 = int(input('Please enter the first year:'))
year2 = int(input('Please enter the second tear:'))
totalDays = 0
days = 0
currYear = year1
while currYear != year2:
    if (currYear % 400) == 0:
        days = 365
    else:
        if currYear % 100 != 0:
            if currYear % 4 == 0:
                days = 366
            else:
                days = 365
        else:
            days = 365
    totalDays += days
    currYear += 1
print('There are %d days form January 1st of %d to January 1st of %d.' %(totalDays, year1, year2))