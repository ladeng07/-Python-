from bs4 import BeautifulSoup
import requests
import re


login_url = 'https://accounts.pixiv.net/api/login?lang=zh'
def get_html(url):
    res = requests.get(url)
    return res.text

def get_soup(html):return BeautifulSoup(html,'lxml')

'''data={
    'pixiv_id':'2312936963@qq.com',
    'captcha':'',
    'g_recaptcha_response':'',
    'password':'hnx12345',
    'post_key':'8fd175a156be871093768b93aa9574df',
    'source':'pc',
    'ref':'wwwtop_accounts_index',
    'return_to':'https://www.pixiv.net/'
    }
headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5193.400 QQBrowser/10.0.1066.400','referer':'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'}
s = requests.session()
s.post(login_url,headers=headers,data=data)
#url = 'https://www.pixiv.net/showcase/a/3638'
url = 'https://www.pixiv.net/'
soup = get_soup(get_html(url))
l =soup.body.find_all('img')
h = s.get('https://www.pixiv.net/')'''
a = requests.get('https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index').text
