"""
The program will use urllib to read the HTML from the data files below, extract the href= values from the anchor tags,
scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat
the process a number of times and report the last name you find.
"""

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# <li style="margin-top: 7px;"><a href="http://py4e-data.dr-chuck.net/known_by_Aniqa.html">Aniqa</a></li>

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count:'))
position = int(input('Enter position:'))


for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    number = 0
    for tag in tags:
        number += 1
        if number == position:
            url = tag.get('href')
            if i == int(count)-1:
                print(tag.contents[0])
            break

