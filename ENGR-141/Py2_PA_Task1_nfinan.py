# Activity 2.2.1: Python 2 PA Task 1
# File: Py2_PA_Task1_nfinan.py
# Date: 28 September 2016
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
# Uses Snell's Law to predict the angle and path of a beam of light travelling trough 2 materials
import math
n2 = 1.3
d1 = 5.3
d2 = 7.6
theta1 = math.radians(float(input("Input incoming angle:")))
n1 = float(input("Input n1:"))
if n1 > n2:
    theta_c = math.asin(n2/n1)


    def length_d3(theta1,theta2):
        d3 = (d1 * math.tan(theta1) + (d2 * math.tan(theta2)))
        return d3
    
    def refraction(n1,n2,theta1):

        theta2 = (math.asin((n1 * math.sin(theta1) / n2)))
        return theta2
    
    theta2 = refraction(n1,n2,theta1)
    rtheta2 = round(math.degrees(theta2),1)
    rd3 = round(length_d3(theta1,theta2),1)
    rtheta_c = round(math.degrees(theta_c),1)
    print("There is refraction with a leaving angle of", rtheta2,"degrees")
    print("The ending distance for the light ray is", rd3,"cm")
    print("For these two media, the critical angle is", rtheta_c,"degrees")
    
    
else:
    print("total internal reflection")