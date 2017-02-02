clear
clc
data = load('boltdata.txt');
mean = mean(data);
median = median(data);
Stdev = std(data);
variance = var(data);
Range = range(data);
mode = mode(data);
histogram(data)
plot(data)