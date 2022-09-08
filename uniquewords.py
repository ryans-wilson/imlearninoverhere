file = input ("Enter a File Name: ")
unique = list()
try:
    fstring = open(file)
except:
    print ('File Name Not Found')
    quit()
for line in fstring:
    wds = line.split()
    for wd in wds:
        if wd not in unique:
            unique.append(wd)
print(sorted(unique))
