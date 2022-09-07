from turtle import position
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input('Enter a count - '))
position = int(input('Enter a position - ')) - 1

# Retrieve all of the anchor tags
href = soup('a')


for i in range(count):
    link = href[position].get('href', None)
    print(href[position].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html, 'html.parser')
    href = soup('a')