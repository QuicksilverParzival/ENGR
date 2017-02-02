% Activity 12.3.2: MatLab Post Activity Task 2
% File: ML3_PA_Task2_nfinan.m
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
% calculate the area for 5 interesting regular shapes. and terminate
% program when two nonexistent shapes are requested.
clc
clear
pent = 172.04774;
hex = 259.80762;
hept = 363.39124;
oct = 482.84271;
non = 618.18242;
error = 0;
while error < 2
    inp = lower(input('Name of regular shape:', 's'));
    
    switch inp
        case 'pentagon'
            fprintf('The area of the pentagon is %f m^2.\n', pent)
        case 'hexagon'
            fprintf('The area of the hexagon is %f m^2.\n', hex)
        case 'heptagon'
            fprintf('The area of the heptagon is %f m^2.\n', hept)
        case 'octagon'
            fprintf('The area of the octagon is %f m^2.\n', oct)
        case 'nonagon'
            fprintf('The area of the nonagon is %f m^2.\n', non)
        otherwise
            fprintf('Error, no such shape is found! ')
            error = error + 1;
            switch error
                case 1
                    fprintf('Try again!\n');
            end
    end
end
fprintf('Program terminated.\n')
