rtotal = 0
count = 0
fname = input ('Enter a file name: ')
if fname == 'na na boo boo':
    print ("NA NA BOO BOO TO YOU - you have been punk'd")
    quit()
try:
    fstring = open(fname)
except:
    print ('File not found', fname)
    quit()
for lines in fstring:
    if lines.startswith('X-DSPAM-Confidence'):
        fstrip = lines.find(':')
        data = lines[fstrip+1:]
        fdata = float (data)
        rtotal = rtotal + fdata
        count = count + 1
print (rtotal/count)