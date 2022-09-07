import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total = 0
count = 0
url = input('Enter url: ')

uh = urllib.request.urlopen(url, context=ctx)
print('Retrieving', url)

data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
#print(info)

for item in info['comments']:
    num = item['count']
    icount = int(num)
    total = total + icount
    
print (total)