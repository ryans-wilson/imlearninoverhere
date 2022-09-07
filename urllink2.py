from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

total = 0
for line in soup:
    if len(line) > 1:
        sline = (line.decode().strip())
        x = re.findall ('>([\d]+)<', sline)
        for values in x:
            y = float(values)
            total = total + y

print(total)