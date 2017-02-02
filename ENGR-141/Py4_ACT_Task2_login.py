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
with open('Py4_ACT_Task2_input.txt', 'r+') as i:
    ln1 = str(i.readline())
    ln2 = str(i.readline())
    ln3 = str(i.readline())
    ln4 = str(i.readline())
    # close
    
print(ln1 + ln2 + ln3 + ln4)