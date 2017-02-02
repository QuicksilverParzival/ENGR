clc
clear
%constants
DOsat = 9;
k1 = 0.2;
k2 = 0.4;
% test variables
Location = 1
Time = 14
Lo = 20
Do = 4
%calculation
DOa = DOsat - ((k1 * Lo) / (k2 - k1) * (exp(-k1 * Time) - exp(-k2 * Time)));
DO = DOa - (Do * exp(-k2 * Time));
fprintf('The concentration of DO is %f [mg/L]',DO)