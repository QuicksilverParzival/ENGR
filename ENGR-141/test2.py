import csv
import math
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

#for loop to calculate sums
#int() truncates, do we want to float() instead? 
#can we get our input files in the google drive?

with open('Print_Head.csv', 'r') as csvfile:
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
        sum_lnx2 += (math.log(float(num[0])) ** 2)
        sum_lnyx += (math.log(float(num[1])) * float(num[0]))
        sum_lnylnx += (math.log(float(num[0])) * math.log(float(num[1])))
        numLines += 1
        
print(sum_x)
print(sum_x2)
print(sum_y)
print(sum_xy)
print(sum_lny)
print(sum_lnx)
print(sum_lnyx)
print(sum_lnx2)
print(sum_lnylnx)
print(numLines)
