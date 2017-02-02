clc
clear
Weight = 0.5;
while Weight <= 5.5
    if Weight <= 1
        Price = 3.99;
    elseif Weight <= 2
        Price = 4.99;
    elseif Weight <= 3
        Price = 5.99;
    elseif ((10 > Weight) & (Weight > 3))
        Price = 5.99 + (Weight - 3) * 2.99;
    else
        Price = string(5.99 + (Weight - 3) * 2.99) + ' X';
    end
    Weight = Weight + 1;
end