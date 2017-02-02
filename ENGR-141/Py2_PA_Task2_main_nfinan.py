# Activity 2.2.2: Python 2 PA Task 2 main
# File: Py2_PA_Task2_main_nfinan.py
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
# Calculates pressure using ideal gas law and corrects temperature to stay within bounds of 1.1 atm to 1.2 atm
from Py2_PA_Task2_functions_nfinan import pressure
from Py2_PA_Task2_functions_nfinan import required_temperature
from Py2_PA_Task2_functions_nfinan import temperature_increment
from Py2_PA_Task2_functions_nfinan import new_pressure
r = 0.0820574587
v = 18
a = 6.49
b = 0.0652
t1 =float((input("Input Initial Temperature in Kelvin:")))
t1_int = int(t1)
P = pressure(t1,v,a,b,r)
t2 = required_temperature(P,t1,v,a,b,r)
tc = temperature_increment(t1,t2)
P2 = new_pressure(t2,v,a,b,r)
print("Initial conditions:")
print("Volume = ", v,"L/mol")
print("Initial temperature = ", t1_int,"K")
print("Parameter a = ", a,"L^2 atm / mol^2")
print("Parameter b = ", b,"L / mol")
print("Resulting pressure = ", round(P,2),"atm")
print("Required temperature increment for in-range pressure = ",round(tc,1),"K")
print("New temperature = ", round(t2,1),"K")
print("New pressure = ", round(P2,1),"atm")
