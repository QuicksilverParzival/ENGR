import csv
with open('Print_Head.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        n = ', '.join(row)
        print(row)
        print(type(n))