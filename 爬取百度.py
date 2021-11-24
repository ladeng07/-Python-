import urllib.request
import json

url = 'http://fanyi.baidu.com/v2transapi'
data = {}

data['from'] = 'zh'
data['to'] = 'en'
data['query'] = '小驾驭'
data['simple_means_flag'] = '3'
data['sign'] = '9730.312627'
data['token'] = '59d6845b100859016327afc2f87387cc'
data = urllib.parse.urlencode (data).encode('utf-8')


response = urllib.request.urlopen (url,data)
html = response.read ().decode('utf-8')

html = json.loads(html)
print ('翻译的结果:'+html['query'])
html
