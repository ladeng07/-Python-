import urllib.request
import requests, re


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5193.400 QQBrowser/10.0.1066.400')
    html = urllib.request.urlopen(url).read().decode('GBK')
    return html


def get_fenlei(num):
    if str(num).isdigit() and num <= 20:
        url = 'https://www.dy2018.com/' + str(num) + '/'
        return url

    else:
        print('请输入一个有效数字!!')


def get_url(url):
    global dylist, addrslist
    html = open_url(url)
    r = re.compile(r'ulink" title="([^"]+)">')
    a = r'a href="([^"]+)" class="ulink"'
    dylist = re.findall(r, html)
    # print (len(dylist))
    addrslist = re.findall(a, html)
    # print (len(addrslist))
    count = 0
    for each in dylist:
        print(str(count) + ':' + each)
        count += 1
    return fanye(input('请输入电影的序号或翻页 上一页/下一页(L/N):'))


def fanye(result):
    if result.isdigit() and int(result) <= 29:
        url = 'https://www.dy2018.com' + addrslist[int(result)]
        return url
    elif result == 'L' or result == 'l':
        if page == 1:
            print ('无法翻到上一页,请输入一个有效数字哦~')
            return fanye(input('请输入电影的序号或翻页 上一页/下一页(L/N):'))

        else:
            page -= 1
            if page == 1:
                return get_url (url1)
            else:
                return get_url(url1 + '/index_' + str(page) + '.html')
    elif result == 'N' or result == 'n':
        page += 1
        return get_url(url1 + '/index_' + str(page) + '.html')
    else:
        print('这不是有效操作')
        return fanye(input('请输入电影的序号或翻页 上一页/下一页(L/N)'))

def get_sth(html):
    t = r'<p>([^"]+)</p>'
    filmlist = re.findall(t, html)
    for each in filmlist:
        each = each.replace ('<p>',' ')
        each = each.replace ('</p>',' ')
        print (each)
    print ('输入M返回主页面：')
    m = input('>>>')
    if m == 'M''or m == 'm'':
        main ()
    else:
        print （"这不是有效操作")


def main():
    global page,url1
    page = 1
    print ('''================================================================================
                            电影分类表：
                0 == 剧情片          11 == 音乐题材电影
                1 == 喜剧片          12 == 传记片
                2 == 动作片          13 == 历史片
                3 == 爱情片          14 == 战争片
                4 == 科幻片          15 == 犯罪片
                5 == 动画片          16 == 奇幻电影
                6 == 悬疑片          17 == 冒险电影
                7 == 惊悚片          18 == 灾难片
                8 == 恐怖片          19 == 武侠片
                9 == 纪录片          20 == 古装片
               *10 == 同性题材电影
================================================================================
               ''')
    url1 = get_fenlei(int(input('请输入电影类别序号：')))
    url = get_url(url1)
    print (url)
    html = open_url(url)
    get_sth (html)

if __name__ == '__main__':
    main ()
