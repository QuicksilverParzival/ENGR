% MatLab Post Activity Task1B
% File: ML1_PA_Task1b_nfinan.m
% Date: 16 November 2016
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
% Calculates the Cross-sectional area of an I-beam from inputted
% Height, Width, and Thickness values.
function output = ML1_PA_Task1b_nfinan(height, width, thickness)
    %calculates surface area
    vert = (height - (2 * thickness)) * thickness;
    horz = width * thickness;
    area = vert + 2 * horz;
    %print height, weight, etc.
    fprintf('Height = %.2f ft\n', height)
    fprintf('Width = %.2f ft\n', width)
    fprintf('Thickness = %.3f ft\n', thickness)
    fprintf('Cross-sectional area = %.2f sq. ft\n', area)
    %sets output as area so the function can be called
    output = area;
end