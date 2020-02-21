import tkinter
from tkinter.filedialog import askdirectory
from tkinter.scrolledtext import ScrolledText
import urllib.request
import os,re


folder='F://imgs'
root = tkinter.Tk()
tkinter.root.title('爬取贴吧 V1.0')
tkinter.root.geometry('512x300') 

bglabel = tkinter.Label(root)
bglabel.pack(side=TOP)

text = tkinter.ScrolledText(root,width=80,height=20)
text.pack(expand=1,fill='both')

url_label=tkinter.Label(bglabel,text='输入链接:',fg='blue',padx=0)
url_label.grid(row=0,column=0,sticky=W)

url_entry = tkinter.Entry(bglabel,width=40)
url_entry.grid(row=0,column=1)

f_label=tkinter.Label(bglabel,text='*选择保存地址\n(默认在F://imgs)',fg='blue',padx=0)
f_label.grid(row=1,column=0,sticky=W)

f_entry = tkinter.Entry(bglabel,width=40)
f_entry.grid(row=1,column=1)

def c_folder():
    global folder
    f_entry.delete(0,END)
    folder = askdirectory()
    f_entry.insert(END,folder)

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
    global c
    html = get_url (url)
    imglist = get_img (html)
    for each in imglist:
        if c == 1:
            filename=each.split('/')[-1]
            urllib.request.urlretrieve(each,filename)
            text.insert(END,each+'\n')
            text.see(END)
            text.update()
        else:
            break

def main(url):
    global c
    count = 1
    page = get_page(get_url(url))
    while count - 1 != get_page(get_url(url)) and c == 1:
        text.insert(END,'此贴共有%d页，现在是%d页\n' % (page,count))
        text.update()
        url1 = url + '?pn=' + str(count)
        download (url = url1,folder=folder)
        count += 1
        time.sleep(1)
    text.insert(END,'DONE!')
    text.see(END)

def start():
    global folder,c
    if url_entry.get() != '':
        text.delete(1.0,END)
        text.insert(END,'正在开始爬取.......\n')
        text.update()
        c = 1
        try:
            os.chdir (folder)
        except FileNotFoundError:
            os.mkdir (folder)
            os.chdir (folder)
        count = 1
        url = url_entry.get()
        main(url)
    else:
        text.insert(END,'请输入链接！\n')


def stop():
    global c
    c = 0
    text.insert(END,'正在停止......\n')


tkinter.Button(bglabel,text='...',command=c_folder,height=1,width=3).grid(columnspan=2,row=1,column=3)

tkinter.Label(bglabel,width=50,height=1).grid(row=2,column=1)

tkinter.Button(bglabel,text='开始爬取',command=start).grid(row=3,column=0,sticky=E)
tkinter.Button(bglabel,text='停止爬取',command=stop).grid(row=3,column=1,sticky=W)

tkinter.mainloop()
