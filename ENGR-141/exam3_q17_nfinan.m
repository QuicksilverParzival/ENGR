% Exam 3 Qestion 17
% File: exam3_q17_nfinan.m
% Date: 14 December 2016
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
% Convert uits to metric
clc
clear
% get user inputs
lenghtUS = input('Enter the length: ');
unitUS = input('Enter the unit name: ');
% define matrix of unit conversion factors
convFactors = {'inches','feet','yards','miles'
               0.0254,0.3048,0.9144,1609.344};
% if proper unit conversion is requested find right factor
factor = 0;
n = 1;
while n < 5
    var = convFactors(n,1);
    if var == unitUS
        factor = convFactors(n,2);
    end
    n = n + 1;
end
if factor
    f2 = factor * lengthUS;
    fprintf('%f %s equals %.4f meters', lengthUS, unitUS, f2);
else
    fprintf('Length unit not recognized.');
end
    
