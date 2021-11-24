import json
import requests
url='https://api.bilibili.com/x/space/arc/search?mid=34625132&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'

def get_json(url):
    r=requests.get(url)
    return json.loads(r.text)

def output(js):
    return js['data']['list']['vlist']

s=0
for i in output(get_json(url)):
    print(i['title'],end='')
    s+=i['play']
    print('   '+str(i['play']))
print(s)
