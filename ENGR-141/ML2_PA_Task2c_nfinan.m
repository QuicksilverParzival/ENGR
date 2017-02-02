% MatLab Post Activity Task 2c
% File: ML2_PA_Task2c_nfinan.m
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
% Displays Multiple digit numerical input like an alarm clock display.
function display =  ML2_PA_Task2c_nfinan(val)
    array = [1 1 1 0 1 1 1
             0 0 1 0 0 1 0
             1 0 1 1 1 0 1
             1 0 1 1 0 1 1
             0 1 1 1 0 1 0
             1 1 0 1 0 1 1
             1 1 0 1 1 1 1
             1 0 1 0 0 1 0
             1 1 1 1 1 1 1
             1 1 1 1 0 1 0];
    val = num2str(val);
    val1 = str2double(val(1)) + 1;
    val2 = str2double(val(2)) + 1;
    cell1 = array(val1,:);
    cell2 = array(val2,:);
    display = [cell1;cell2];
end