% Activity 12.3.1: Stats ACT Task 1
% File: Stats_ACT_Task1_nfinan.m
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
file = fopen('Activity1Data.txt', 'r');
[array, count] = fscanf(file, '%d : %d', [2, inf]);
array = array';
i = 1;
while i <= count / 2
    array(i,2) = array(i,2) / 60;
    newarray(i) = array(i,1) + array(i,2);
    i = i + 1;
end
newarray = newarray';
mean = mean(newarray);
median = median(newarray);
mode = mode(newarray);
variance = var(newarray);
STD = std(newarray);

meandec = mod(mean, 1) * 60;
meanwhole = mean - mod(mean, 1);
mean2 = strcat(num2str(meanwhole),':',num2str(meandec))
