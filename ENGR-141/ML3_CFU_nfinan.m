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
% Calculates The Dissolved oxygen in the wbash River on a range of days
clc
clear
%constants
DOsat = 9;
k1 = 0.2;
k2 = 0.4;
Do = 4;
Lo = 25;
t = 1;
fprintf('DO in Wabash in mg/L:\n')
fprintf('Day\tDO\n')
fprintf('-----------\n')
while t <= 20
    DOa = DOsat - ((k1 * Lo) / (k2 - k1));
    DO = DOa * (exp(-k1 * t) - exp(-k2 * t)) - (Do * exp(-k2 * t));
    if (DO > 6) && (DO < 8)
        DO = string(DO) + '*';
    else
        DO = string(DO);
    end
    fprintf('%d\t',t)
    fprintf('%s\n',DO)
    t = t + 1;
end