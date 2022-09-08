import re
print ('This code finds the sum of all the numbers in a text file')
file = input('Input a file name: ')
ofile = open(file)
count = 0
ftotal = 0

for lines in ofile:
    line = lines.rstrip()
    x = re.findall ('([0-9]+)', line)
    if len(x) < 0 : continue
    for values in x:
        y = float(values)
        count = count + 1
        ftotal = ftotal + y

total = int(ftotal)
print ('There are', count, 'number of values with a total of', total)