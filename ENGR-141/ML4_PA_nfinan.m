% MatLab 4 Post Activity Task 1
% File: ML4_PA_Task1_nfinan.m
% Date: 7 December 2016
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
% Read A File of Power inputs and compute various things. Also outputs to
% both the screen and a new text file.
clc
clear
A = importdata('ML4_PA_input.txt');
array = A.data;
%starting Values
Inv_Req = 0;
Req = 0;
i = 1;
T_Power = 0;
v = 120;
sum_below = 0;
n = 1;

while n <= 10;
    i = 1;
    Inv_Req = 0;
    Req = 0;
    T_Power = 0;
    v = 120;
    sum_below = 0;
    acceptable = 'Y';
    

    while i <= 50;
        p = array(i,n);
        T_Power = p + T_Power;
        r = v ^ 2 / p;
        Inv_Req = 1 / r + Inv_Req;
        if r < 1 * 10 ^ 6
            sum_below = sum_below + 1;
        end

        i = i + 1;
    end
    if ((T_Power <= 2.20) || (T_Power >= 2.60))
        acceptable = 'N';
    end
    Req = 1 / Inv_Req;
    Tarray(n,:) = [T_Power, Req, sum_below];
    Sarray(n,:) = acceptable;
    n = n + 1;
end
%prints to screen
fprintf(['String\t\t1\t\t  2\t\t    3\t\t  4\t\t    5\t\t  6\t\t   '...
    ' 7\t\t  8\t\t    9\t\t  10\n'])

fprintf(['Total\t\t%.2f\t  %.2f\t    %.2f\t  %.2f\t    %.2f\t  %.2f\t'...
    '    %.2f\t  %.2f\t    %.2f\t  %.2f\t\n'...
    ],Tarray(1,1),Tarray(2,1),Tarray(3,1),Tarray(4,1),Tarray(5,1),...
Tarray(6,1),Tarray(7,1),Tarray(8,1),Tarray(9,1),Tarray(10,1))
fprintf('Power?\n')

fprintf(['Equivalent\t%.2d  %.2d  %.2d  %.2d  %.2d  %.2d  %.2d  '...
    '%.2d  %.2d  '...
'%.2d\n'],Tarray(1,2),Tarray(2,2),Tarray(3,2),Tarray(4,2),Tarray(5,2),...
Tarray(6,2),Tarray(7,2),Tarray(8,2),Tarray(9,2),Tarray(10,2))
fprintf('Resistance?\n')

fprintf(['Number of\t%.f        %.f        %.f        %.f        %.f   '...
    '     %.f        %.f        %.f        %.f        %.f\n'...
    ],Tarray(1,3),Tarray(2,3),Tarray(3,3),Tarray(4,3),Tarray(5,3),...
Tarray(6,3),Tarray(7,3),Tarray(8,3),Tarray(9,3),Tarray(10,3))
fprintf('Bulbs with\nR<1e6Ohms?\n')

fprintf(['Acceptable?\t %s         %s         %s         %s         '...
    '%s         %s         %s         %s         %s         %s\n'...
],Sarray(1),Sarray(2),Sarray(3),Sarray(4),Sarray(5),...
Sarray(6),Sarray(7),Sarray(8),Sarray(9),Sarray(10))

%write to file
out = fopen('ML4_PA_nfinan.txt','wt');

fprintf(out,['String\t\t1\t\t  2\t\t    3\t\t  4\t\t    5\t\t  6\t\t   '...
    ' 7\t\t  8\t\t    9\t\t  10\n']);

fprintf(out,['Total\t\t%.2f\t  %.2f\t    %.2f\t  %.2f\t    %.2f\t'...
    '  %.2f\t    %.2f\t  %.2f\t    %.2f\t  %.2f\t\n'...
    ],Tarray(1,1),Tarray(2,1),Tarray(3,1),Tarray(4,1),Tarray(5,1),...
Tarray(6,1),Tarray(7,1),Tarray(8,1),Tarray(9,1),Tarray(10,1));
fprintf(out,'Power?\n');

fprintf(out,['Equivalent\t%.2d  %.2d  %.2d  %.2d  %.2d  %.2d  %.2d  '...
    '%.2d  %.2d  '...
'%.2d\n'],Tarray(1,2),Tarray(2,2),Tarray(3,2),Tarray(4,2),Tarray(5,2),...
Tarray(6,2),Tarray(7,2),Tarray(8,2),Tarray(9,2),Tarray(10,2));
fprintf(out,'Resistance?\n');

fprintf(out,['Number of\t%.f        %.f        %.f        %.f        '...
    '%.f        %.f        %.f        %.f        %.f        %.f\n'...
    ],Tarray(1,3),Tarray(2,3),Tarray(3,3),Tarray(4,3),Tarray(5,3),...
Tarray(6,3),Tarray(7,3),Tarray(8,3),Tarray(9,3),Tarray(10,3));
fprintf(out,'Bulbs with\nR<1e6Ohms?\n');

fprintf(out,['Acceptable?\t %s         %s         %s         %s   '...
    '      %s         %s         %s         %s         %s         %s\n'...
],Sarray(1),Sarray(2),Sarray(3),Sarray(4),Sarray(5),...
Sarray(6),Sarray(7),Sarray(8),Sarray(9),Sarray(10));

fclose(out);