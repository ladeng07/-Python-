import urllib.request
import json
import time

while 1:
    url = 'http://fanyi.youdao.com/translate'
    data = {}

    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5193.400 QQBrowser/10.0.1066.400'

    data['i'] = input('输入要翻译:')
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict '
    data['client'] = 'fanyideskweb'
    data['salt'] = '1530936004566'
    data['sign'] = '0ade99022af93672c5b6f0e576cdf5a3'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTIME'
    data['typoResult'] = 'ture'
    data = urllib.parse.urlencode (data).encode('utf-8')

    req = urllib.request.Request (url,data,head)
    response = urllib.request.urlopen (req)
    html = response.read ().decode('utf-8')

    #print (html)

    html = json.loads(html)
    print ('翻译的结果:'+html['translateResult'][0][0]['tgt'])
    time.sleep (3)
