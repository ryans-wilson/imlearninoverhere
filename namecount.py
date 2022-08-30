file = input('Enter a file name')
namelist = list()
count = 0
try:
    op = open(file)
except:
    print ('File Does Not Exist')
    quit()
for lines in op:
    lines = lines.rstrip()
    if lines.startswith('From '):
        wd = lines.split()
        email = wd[1]
        esplit = email.split('@')
        name = esplit[0]
        count = count + 1
        if name not in namelist:
            namelist.append(name)
print (namelist, count)
