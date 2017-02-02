% Activity 13.2.2: MatLab CFU
% File: ML4_CFU_nfinan.m
% Date: 30 November 2016
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
% Separates poorly formatted numerical data from ##.#####.#####.### to a
% more viewable ##.### format.
clear
clc
file = fopen('ML4_CFU_input.txt','r');%data file
[array, Count] = fscanf(file,['%2d . %3d'],[2, inf]); %scans the file for
%two integers then a decimal, then 3 integers.
array = array';%corrects the dimensions of the array
i = 1;
while i <= (Count / 2)
    %prints each row of the array while adding back the decimal point
    fprintf('%d.%d\n', array(i,1), array(i,2))
i = i + 1;
end

fclose(file);