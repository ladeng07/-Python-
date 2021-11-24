import requests
import re,os,shutil
import urllib.request
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5193.400 QQBrowser/10.0.1066.400'}
tp = ['breasts','long_hair','honkai_impact+']
def get_html(url):
    res = requests.get(url,headers=headers)
    return res.text

def get_url(url):
    r = get_html(url)
    t = re.compile(r'<span class="plid">#pl ([^"]+)</span>')
    return re.findall(t,r)

def download(url):
    t = re.compile(r'href="([^"]+)" id="png">')
    l = re.findall(t,get_html(url))
    if l == []:
        l = re.findall(r'href="([^"]+)" id="highres">',get_html(url))
    filename = l[-1].split('/')[-1]
    urllib.request.urlretrieve(l[-1],filename)
    
def main(page=2,s_page=1,folder='C:\\爬虫图片'):
    if not os.path.exists(folder):
        os.mkdir(folder)
    os.chdir(folder)
    for i in range(s_page,page+s_page):
        for each in get_url('https://konachan.net/post?page=%d&tags=%s' % (i,tp[2])):
            print(each)
            t = re.compile(r'href="([^"]+)" id="png">')
            l = re.findall(t,get_html(each))
            if l == []:
                l = re.findall(r'href="([^"]+)" id="highres">',get_html(each))
            filename = l[-1].split('/')[-1]
            if not os.path.exists(folder+'\\'+filename):
                download(each)
            
main(int(input('请输入要爬取的页数：')),s_page=1)
