% Activity 12.3.1: MatLab Post Activity Task 1
% File: ML3_PA_Task1_nfinan.m
% Date: 2 December 2016
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
% Reads input file for m, c, and k, contstants and calculates Natural
% Frequency, Damping Ratio, and Damping Frequency
clc
clear

%in = input('Please enter file name\n','s');
in = 'dynamics.txt';
file = fopen(in,'r');
[vals, count] = fscanf(file,'%d',[3,inf]);
vals = vals';
i = 1;
while i <= count / 3
    m = vals(i,1);
    c = vals(i,2);
    k = vals(i,3);
    p = c / m;
    q = k / m;
    wn = sqrt(q);
    ratio = p / (2 * wn);
    wd = wn * sqrt(1 - ratio ^ 2);
    if (m > 0) && (c > 0) && (k > 0)
        fprintf('%d) Natural Frequency = %f rad s-1; ', i, wn)
        fprintf('Damping ratio = %f;\n', ratio)
        
        if p < 1
            fprintf('Damped Frequency = %f rad s-1\n', wd)
            fprintf('System is underdamped.\n')
        elseif p == 1
            fprintf(['System is critically damped; damped frequency '... 
            'does not exist.\n'])
        elseif p > 1
            fprintf(['System is overdamped, damped frequency does '...
            'not exist.\n'])
        else
            fprintf('problem\n')
        end
    else
        fprintf('%d) Error in input values.\n', i)
    end
i = i + 1;
end
fclose(file);