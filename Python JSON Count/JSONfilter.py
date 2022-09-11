import urllib.request
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1623177.json'
uh = urllib.request.urlopen(url)
data = uh.read()

info = json.loads(data)
infocomments = info['comments']
sumlist = list()

for item in infocomments:
    #print(item['count']) #Shows all values of the key 'count'
    sumlist.append(item['count'])

print(sum(sumlist))