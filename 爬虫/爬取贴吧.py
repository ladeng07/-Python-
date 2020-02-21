import urllib.request
import os,re,time,shutil

folder = 'F://imgs'
def get_url (url):
    req = urllib.request.Request (url)
    req.add_header ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5193.400 QQBrowser/10.0.1066.400')
    response = urllib.request.urlopen (url)
    html = response.read().decode ('utf-8')
    return html

def get_img (html):
    q = r'<img class="BDE_Image"[\sA-Za-z0-9="_]+src="([^"]+\.jpg)"'
    img_list = re.findall (q,html)
    return img_list

def get_page(html):
    t = r'<span class="red">(\d+)</span>'
    page = re.findall(t,html)
    return int(page[0])

def download (url,folder):
    u = urllib.request.urlretrieve
    html = get_url (url)
    imglist = get_img (html)
    for each in imglist:
        filename=each.split('/')[-1]
        u(each,filename)
        print(each)
	    
if os.path.exists(folder):
    shutil.rmtree(folder)
os.mkdir (folder)
os.chdir (folder)
count = 1
url = input('输入链接：')
while count - 1 != get_page(get_url(url)):
    url1 = url + '?pn=' + str(count)
    print(url1)
    download (url = url1,folder=folder)
    count += 1
    time.sleep(1)
