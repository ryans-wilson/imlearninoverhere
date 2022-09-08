name = input("Enter file: ")
try:
    handle = open(name)
except:
    print ('Error - Please Enter a Valid File Name')
    quit()
d = {}

for lines in handle:
    if lines.startswith('From '):
        words = lines.split()
        word = words[1]
        d[word] = d.get(word,0) + 1

lst = list()
for key, val in list(d.items()):
    lst.append((val, key))
lst.sort(reverse=True)

for key, val in lst[:1]:
    print(key, val)