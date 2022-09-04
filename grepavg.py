import re
print ('This code finds the averages of all values of the "New Revisions"')
file = input('Input a file name: ')
ofile = open(file)
count = 0
total = 0

for lines in ofile:
    line = lines.rstrip()
    x = re.findall ('New Revision: ([0-9]+)', line)
    if len(x) != 1: continue
    y = float(x[0])
    count = count + 1
    total = total + y
favg = total/count
avg = int(favg)
print (avg)