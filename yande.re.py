'''import requests
import re,os,time
import urllib.request

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5193.400 QQBrowser/10.0.1066.400',
          'Referer':'https://yande.re/post'}

def get_html(url):
    res = requests.get(url,headers=header)
    return res.text
def download(url):
    t = re.compile(r'href="([^"]+)">Download larger')
    l = re.findall(t,get_html(url))
    if l == []:
        l=re.findall(r'id="highres" href="([^"]+)">Image',get_html(url))
    filename = l[0].split('/')[-1]
    urllib.request.urlretrieve(l[0],filename)
def get_num(url):
    r = get_html(url)
    t = re.compile(r'/post/show/(\d+)')
    return set(re.findall(t,r))
def main(page=2,s_page=1,folder='F:\\good_imgs'):
    if not os.path.exists(folder):
        os.mkdir(folder)
    os.chdir(folder)
    for each in range(s_page,int(page)+s_page):
        for i in get_num('https://yande.re/post?page=%d'% each):
            url = 'https://yande.re/post/show/'+i
            print(url)
            download(url)
            time.sleep(2)
main(input('请输入要爬取的页数：'),s_page=1)
'''
import requests
import re,os,time
import urllib.request

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5193.400 QQBrowser/10.0.1066.400',
          'Referer':'https://yande.re/post'}

def get_html(url):
    res = requests.get(url,headers=header)
    return res.text
def download(url):
    t = re.compile(r'href="([^"]+)">Download larger')
    l = re.findall(t,get_html(url))
    if l == []:
        l=re.findall(r'id="highres" href="([^"]+)">Image',get_html(url))
    filename = l[0].split('/')[-1]
    urllib.request.urlretrieve(l[0],filename)
def get_num(url):
    r = get_html(url)
    t = re.compile(r'/post/show/(\d+)')
    return set(re.findall(t,r))
def main(page=2,s_page=1,folder='C:\\good_imgs'):
    if not os.path.exists(folder):
        os.mkdir(folder)
    os.chdir(folder)
    for each in range(s_page,int(page)+s_page):
        for i in get_num('https://yande.re/post?page=%d'% each):
            url = 'https://yande.re/post/show/'+i
            print(url)
            download(url)
            time.sleep(2)
main(input('请输入要爬取的页数：'),s_page=1)
