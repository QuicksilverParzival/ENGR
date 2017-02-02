# MatLab Post Activity Task1D
# File: ML1_PA_Task1d_nfinan.py
# Date: 16 November 2016
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
# Calculates the Cross-sectional area of an I-beam as well as stress and load.
def getIBeam(height, width, thickness):
    #calculates surface area of beam
    vert = (height - (2 * thickness)) * thickness
    horz = width * thickness
    area = vert + 2 * horz
    #prints results
    print('Height = %.2f ft'%height)
    print('Width = %.2f ft'%width)
    print('Thickness = %.3f ft'%thickness)
    print('Cross-sectional area = %.2f sq. ft'%area)
    return area
    
#requests input for height, width, etc.
list = input('Input height, width and thickness of the I-beam (in ft): ')
list = list.strip().split()
#read inputted values as list
h = int(list[0])
w = int(list[1])
t = int(list[2])
#input load
load = int(input('Input the applied load (in lbs): '))
print('... running')
#calculate stress
area = getIBeam(h, w, t)
stress = load / area
input = str(input('Enter the file name where you wish to save results: '))
height2 = str(round(h,2))
width2 = str(round(w,2))
thickness2 = str(round(t,3))
area2 = str(round(area,2))
load2 = str(round(load,2))
stress2 = str(round(stress,2))
#creates lines to be printed in output file
line1 = 'For a beam with a height of '+ height2 +' ft, width of '+ width2 +' ft and a thickness\r\n'
line2 = 'of '+ thickness2  +' ft, the cross-sectional area is '+ area2 +' sq. ft.\r\n'
line3 = 'For an applied load of '+ load2 +' lbs, the stress on the I-beam is '+ stress2 +' psf.'
outSequence = [line1, line2, line3]
#opens/creates inputted file as write
with open(input, 'w') as output:
    output.writelines(outSequence)
    
    #close
print('... output written to file ', input ,'.')