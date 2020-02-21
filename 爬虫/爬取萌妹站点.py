import requests
import re,os
import urllib.request
def get_html(url):
    res = requests.get(url)
    return res.text
def download(url):
    t = re.compile(r'href="([^"]+)">Download larger')
    l = re.findall(t,get_html(url))
    if l == []:
    	 l=re.findall(r'id="highres" href="([^"]+)">Image',get_html(url))
    filename = l[0].split('/')[-1]
    #print(l[0].replace('jpeg','image'))
    urllib.request.urlretrieve(l[0].replace('jpeg','image'),filename)
def get_num(url):
    r = get_html(url)
    t = re.compile(r'/post/show/(\d+)')
    return set(re.findall(t,r))
def main(page=2,s_page=1,folder='//storage//emulated//0//good_imgs'):
    if not os.path.exists(folder):
    	os.mkdir(folder)
    os.chdir(folder)
    for each in range(s_page,int(page)+s_page):
        for i in get_num('https://yande.re/post?page=%d'% each):
            url = 'https://yande.re/post/show/' + i
            print(url)
            download(url)
main(input('一页约有40张图片，请输入要爬取的页数：'),s_page=1)
