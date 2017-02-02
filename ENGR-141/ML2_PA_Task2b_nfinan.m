% MatLab Post Activity Task 2b
% File: ML2_PA_Task2b_nfinan.m
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
% Displays single digit numerical input like an alarm clock display.
function display =  ML2_PA_Task2b_nfinan(val)
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
    val = val + 1;
    display = array(val,:);

end