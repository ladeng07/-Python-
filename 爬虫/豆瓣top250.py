from bs4 import BeautifulSoup
import requests
import re

count = 0
def get_html(url):
    res = requests.get(url)
    return res.text
def get_soup(html):return BeautifulSoup(html,'lxml')
def get_25(url):
    soup = get_soup(get_html(url))
    name = soup.body.find_all('span',attrs={'class':'title'})
    for i in name:
        if '/' in i.string:
            name.remove(i)
    actors = soup.body.find_all('p',attrs={'class':''})
    r_num = soup.body.find_all('span',attrs={'class':'rating_num'})
    inq = soup.body.find_all('span',attrs={'class':'inq'})
    if 25 - len(inq) != 0:
        for i in range(25-len(inq)):
            inq.append(inq[-1])
    for i in range(25):
        print('---%d---' % i + '<<' + name[i].string + '>>'+' 豆瓣Top %d'%(count+i+1))
        for c in actors[i].strings:
            print('*'+c.replace('\n','').replace(' ',''))
        print('*评分: ' + r_num[i].string + '分')
        print('*评价: "' + inq[i].string + ' "')
        print('*'*40)
    print('当前页数为第%d/10页' % ((count+25)/25))

def get_url(html):
    return re.findall(r'<a href="([^"]+)" class="">',html)

def get_page(result):
    global count
    if count > 24 and (result == 'L'  or result == 'l'):
        count -= 25
        main()
    elif count < 24 and (result == 'L'  or result == 'l'):
        print('当前页数为第一页，无法继续往前，')
        main()
    elif count < 224 and (result == 'N'  or result == 'n'):
        count += 25
        main()
    elif count > 224 and (result == 'N'  or result == 'n'):
        print('当前页数为最后一页，无法继续往后，')
        main()
    else:
        print('这不是有效输入，')
        main()

def get_message(url):
    global count
    soup = get_soup(get_html(url))
    title = soup.body.find('span',attrs={'property':'v:itemreviewed'})
    hidden = soup.body.find('span',{'class':'all hidden'})
    tp = soup.body.find_all('span',attrs={"property":"v:genre"})
    date = soup.body.find_all('span',attrs={"property":"v:initialReleaseDate"})
    lst = soup.body.find_all('span',attrs={'class':'pl'})
    print('*'*30+'\n\n' +title.string + '\n\n'+ '*'*30+'\n')
    print('导演 : ',end='')
    for i in lst[0].next_sibling.next_sibling.strings:
        print(i,end='')
    print('\n')
    print('编剧 : ',end='')
    for i in lst[1].next_sibling.next_sibling.strings:
        print(i,end='')
    print('\n')
    print('主演 : ',end='')
    for i in lst[2].next_sibling.next_sibling.strings:
        print(i,end='')
    print('\n')
    print('类型 : ',end='')
    for i in tp:
        print(i.string + ' / ',end='')
    print('\n')
    print('制片国家/地区 : '+str(lst[4].next_sibling)+'\n')
    print('语言 : '+str(lst[5].next_sibling)+'\n')
    print('上映日期 : ',end='')
    for i in date:
        print(i.string,end='')
    print('\n')
    print('片长 : '+ soup.body.find('span'\
                                  ,attrs={'property':'v:runtime'}).string+'\n')
    print('又名 : '+str(lst[8].next_sibling)+'\n')
    print('---剧情简介---')
    if hidden != None:
        for i in hidden.strings:
            print(i)
    else:
        for i in soup.body.find('span',attrs={'property':'v:summary'}):
            print(str(i).replace('<br/>','').replace(' ',''))
    r = input('输入Q返回列表或输入M返回第一页: ')
    if r == 'q' or r == 'R':
        main()
    else:
        count = 0
        main()

def main():
    url = 'https://movie.douban.com/top250?start='+str(count)+'&filter='
    get_25(url)
    r = input('输入电影序号或上一页或下一页 L/N : ')
    if r.isdigit():
        get_message(get_url(get_html(url))[int(r)])
    else:
        get_page(r)
main()
