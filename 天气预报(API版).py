import requests
import json

def get_city():
    r = input('输入要查询的地点\n>>>')
    return 'https://www.apiopen.top/weatherApi?city=%s' % r
def main(url):
    res = requests.get(url)
    js = json.loads(res.text)
    l = js['data']['forecast']
    l.insert(0,js['data']['yesterday'])
    print ('---昨天，今天及未来四天天气预报---')
    for i in l:
        for key in i.keys():
            if key=='date':print('日期: ',i[key])
            elif key == 'high':print('高温: ',i[key].replace('高温',''))
            elif key == 'low':print('低温:',i[key].replace('低温',''))
            elif key == 'fx' or key == 'fengxiang':print('风向: ',i[key])
            elif key == 'fl' or key == 'fengli':print('风力: ',i[key])
            elif key == 'type':print('天气: ',i[key])
        print('*'*15)
    print(js['data']['ganmao'],'\n'+'当前体感温度: ',js['data']['wendu']+' ℃')
while 1:
    try:
        main(get_city())
    except TypeError:
        print('对不起，查询不到该地点.')
