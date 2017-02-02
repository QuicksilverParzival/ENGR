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
        sum_lnx2 += math.log(float(num[0])) ** 2
        sum_lnyx += (math.log(float(num[1])) * float(num[0]))
        sum_lnylnx += (math.log(float(num[0])) * math.log(float(num[1])))
        numLines += 1

#Linear Model
a0lin = ((sum_y * sum_x2) - (sum_x * sum_xy)) / ((numLines * sum_x2) - (sum_x * sum_x))
a1lin = ((numLines * sum_xy) - (sum_y * sum_x)) / ((numLines * sum_x2) - (sum_x * sum_x))
##calculate r^2 value here and store as 'r2lin' before next step

#Exponential Model
a0exp = math.exp(((sum_lny * sum_x2) - (sum_x * sum_lnyx)) / (sum_x2 - (sum_x * sum_x)))
a1exp = ((numLines * sum_lnyx) - (sum_lny * sum_x)) / ((numLines * sum_x2) - (sum_x * sum_x))
##calculate r^2 value here and store as 'r2exp' before next step

#Power model
a0pow = math.exp(((sum_lny * sum_lnx2) - (sum_lnx * sum_lnylnx)) / (sum_lnx2 - (sum_lnx * sum_lnx)))
a1pow = ((numLines * sum_lnylnx) - (sum_lny * sum_lnx)) / ((numLines * sum_lnx2) - (sum_lnx * sum_lnx))
##calculate r^2 value here and store as 'r2pow' before next step'''

#Chooses whcih model to use from the highest r^2 value
if r2lin > r2exp:
    if r2lin > r2pow:
        print('Linear model to be used')
        a0 = a0lin
        a1= a1lin
    else:
        print('Power model to be used')
        a0 = a0pow
        a1 = a1pow
if r2exp > r2lin:
    if r2exp > r2pow:
        print('Exponential model to be used')
        a0 = a0exp
        a1 = a1exp

print('a0 value for model:', a0lin)
print('a1 value for model:', a1lin)