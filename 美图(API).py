import requests
import json,urllib.request
import os

if not os.path.exists('F://meitu'):
    os.mkdir('F://meitu')
os.chdir('F://meitu')
for i in range (7,30):
    url = 'https://www.apiopen.top/meituApi?page=%d' % i
    res = requests.get(url)
    js = json.loads(res.text)
    for i in js['data']:
        name = i['url'].split('/')[-1]
        urllib.request.urlretrieve(i['url'],name)
        print(i['createdAt'])

