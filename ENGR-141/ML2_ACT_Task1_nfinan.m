clc
clear
X = [-pi:0.1:pi];
Y = X .^ 1 - ((X .^ 3) / factorial(3)) + ((X .^ 5) / factorial(5))...
    - ((X .^ 7) / factorial(7));
plot(X,Y)
xlabel('x values')
ylabel('y values')
title('Sine Graph')