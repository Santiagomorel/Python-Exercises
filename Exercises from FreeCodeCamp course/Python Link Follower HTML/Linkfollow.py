import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/known_by_Antoni.html'
position = 18
count = 7
i = 0
print(url)

while i < count:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    j = 1
    tags = soup('a')
    for tag in tags:
        if j < position:
            j += 1
            continue
        elif j == position:
            print(tag.get('href', None))
            url = tag.get('href', None)
            j += 1
        else:
            break
    i += 1