% MatLab Post Activity Task1C
% File: ML1_PA_Task1c_nfinan.m
% Date: 16 November 2016
% By: Nicholas Finan
% nfinan
% Section: 3
% Team: 38
%
% ELECTRONIC SIGNATURE
% Nicholas Finan
%
% The electronic signature above indicates that the program
% submitted for evaluation is my individual work. I have
% a general understanding of all aspects of its development
% and execution.
%
% Calculates the Cross-sectional area of an I-beam as well 
% as stress and load.
clc   %clears screen and variables
clear
%request imputs
h = input('Input the height of the I-beam (in ft): ');
w = input('Input the width of the I-beam (in ft): ');
t = input('Input the thickness of the I-beam (in ft): ');
load = input('Input the applied load (in lbs): ');
fprintf('... running\n')
%calculates stress
stress = load / ML1_PA_Task1b_nfinan(h, w, t);
fprintf('The stress acting on the I-beam is %.2f psf.\n', stress)
