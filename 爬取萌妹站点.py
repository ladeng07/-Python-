import requests
import re,os
import urllib.request
import sys
import you_get
def get_html(url):
    res = requests.get(url)
    return res.text
def download(url,path):
    t = re.compile(r'href="([^"]+)">Download larger')
    l = re.findall(t,get_html(url))
    if l == []:
    	 l=re.findall(r'id="highres" href="([^"]+)">Image',get_html(url))
    filename = l[0].split('/')[-1]
    print(l[0].replace('jpeg','image'))
    sys.argv=['you-get','-o',path,l[0].replace('jpeg','image')]
    you_get.main()
    #urllib.request.urlretrieve(l[0].replace('jpeg','image'),filename)
def get_num(url):
    r = get_html(url)
    t = re.compile(r'/post/show/(\d+)')
    return set(re.findall(t,r))
def main(page=2,s_page=1,folder='C:\爬虫图片\yande',tag=''):
    if not os.path.exists(folder):
    	os.mkdir(folder)
    os.chdir(folder)
    for each in range(s_page,int(page)+s_page):
        for i in get_num('https://yande.re/post?page=%d'% each + tag):
            url = 'https://yande.re/post/show/' + i
            print(url)
            download(url,path=folder)

c=input('选择模式，1=标签模式')
if c == '1':
    print('0=honkai_impact')
    c=input('选择标签 ：')
    l=['&tags=honkai_impact']
    main(input('一页约有40张图片，请输入要爬取的页数：'),s_page=1,tag=l[int(c)])
main(input('一页约有40张图片，请输入要爬取的页数：'),s_page=1)
