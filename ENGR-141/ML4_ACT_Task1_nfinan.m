% Activity 13.2.1: MatLab ACT
% File: ML4_ACT_Task2_nfinan.m
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
% Calculates Total Drag Force and Induced Drag for a range of speeds.
clc
clear
file = fopen('ML4_ACT_Task2.txt','r');
[n,m] = size(file);
[array, Count] = fscanf(file,['%f:%s'],[2, inf]);
% array = array';
% disp(array);
% disp(array(1,2));
% disp(Count);
% repeat this
fprintf('Student ID      Grade')
i = 1;
while not(feof(file))
    if array(i,2) == 66
        fprintf(array(i,:))
    end
i = i + 1;
end
fclose(file);