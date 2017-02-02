# Python 4 PA Task 2
# File: Py4_PA_Task2_nfinan.py
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
# Searches for inputted word and calculates the percent abundance of that word
searchWord = input('Enter the search word:')
search = open('Text_File.txt', 'r')
lines = search.readlines()
liness = []
punct = [',','"','.','-','_',':',';','>','<','?','/','!']

sum = 0
n = 0

liness = []
for var in lines:
    if lines.index(var) != lines.index(lines[-1]):
        var2 = var[:-1]
        line = var2
    else:
        line = var
    
    liness.append(line)
liness = str(liness)

for x in punct:
    liness = liness.replace(x,'')
    

liness = liness[1:-1]
linesLower = liness.lower()
linesNew = linesLower.split()

for var in linesNew: 
    if var == searchWord:
        n += 1
    sum += 1
        
search.close()
ave = (n / sum) * 100
print('The search word occurred %.2f%% of the time.' % (ave))