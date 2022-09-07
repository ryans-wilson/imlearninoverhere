import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
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
# print(data.decode())

tree = ET.fromstring(data)
dir = tree.findall('comments/comment')
for items in dir:
    count = items.find('count').text
    count = int (count)
    total = total + count

print(total)