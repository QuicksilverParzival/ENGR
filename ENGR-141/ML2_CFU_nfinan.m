% Activity 12.3.1: MatLab CFU
% File: ML1_CFU_nfinan.m
% Date: 18 November 2016
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
% Outputs Mach Number vs. Pressure
clc
clear
y = 1.4;
M = [1:.1:5];
Po = 10;
P = Po * ((2 * y * (M .^ 2)) - (y - 1) / (y + 1));
plot(M,P)
hold on
Po = 8;
P = Po * ((2 * y * (M .^ 2)) - (y - 1) / (y + 1));
plot(M,P)
legend('Altitude 1','Altitude 2')
title('Mach Number vs. Downstream Pressure(psi)')
xlabel('Mach Number')
ylabel('Downstream Pressure(psi)')
hold off
