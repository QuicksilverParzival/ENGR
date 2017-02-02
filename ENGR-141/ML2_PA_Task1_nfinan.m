% MatLab Post Activity Task 1
% File: ML2_PA_Task1_nfinan.m
% Date: 22 November 2016
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
% Calculates Total Drag Force and Induced Drag for a range of speeds.
clc
clear
AR = 3;
e = 0.9;
p = 1.066 * (10 ^ (-3));
Cd0 = 0.018;
S = 610;
L = 1000;
V = [10:5:350];
Cl =  L ./ (0.5 * p * V .^2 * S);
Di = Cl.^2 .* 0.5 .* p .* V.^2 .* S / (pi * e * AR);
D0 = 0.5 * p * V.^2 * S * Cd0;
D = D0 + Di;
plot(V,D)
hold on
plot(V,Di)
legend('Drag Force','Induced Drag')
title('Total Drag Force and Induced Drag Force v. Speed')
xlabel('Speed [ft/s]')
ylabel('Drag Force')
hold off