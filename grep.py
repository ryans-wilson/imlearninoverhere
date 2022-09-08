import re
iregex = input('Enter a regular expression: ')
file = open('mbox.txt')
count = 0
for lines in file:
    lines = lines.rstrip()
    if re.search(iregex, lines):
        count = count + 1
print ('mbox.txt had', count, 'lines that matched', iregex)