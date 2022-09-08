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

bigword = None
bigcount = None
for word in d:
    if bigcount == None or d[word] > bigcount:
        bigcount = d[word]
        bigword = word
    else:
        continue

print(bigword, bigcount)
