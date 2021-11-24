import requests
from bs4 import BeautifulSoup

def get_num():
    file=open('citynumber.txt','r',encoding='gb2312')
    cl = {}
    while 1:
        line = file.readline()
        if not line:
            break
        if line != '\n':
            line = line.replace('\n','')
            line = line.replace(' ','')
            cl[line.split('=')[1]]=line.split('=')[0]
    result = input('请输入要查询天气的城市:')
    if result in cl:
        return cl[result]
    else:
        print('对不起,查询不到该地点')
        get_num()
def main():
    html = requests.get('http://www.weather.com.cn/weather/'+get_num()+'.shtml')
    html.encoding='utf-8'
    soup = BeautifulSoup(html.text,'lxml')
    win = soup.body.find_all('p',attrs={'class':'win'})
    day = soup.body.find_all('li',attrs={'class':'sky'})
    wea = soup.body.find_all('p',attrs={'class':'wea'})
    tem = soup.body.find_all('p',attrs={'class':'tem'})
    win_l = soup.body.find_all('p',attrs={'class':'win'})
    for i in range(7):
        print('时间: '+day[i].h1.string)
        print('天气: '+wea[i]['title'])
        print('温度: '+tem[i].i.string)
        print('风向: '+win[i].em.span['title'])
        print('风力: '+win_l[i].i.string)
        print('**********')
while 1:
    main()
