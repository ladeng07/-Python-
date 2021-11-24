import json
import requests
def get_json(url):
	res=requests.get(url)
	js=json.loads(res.text)
	return js
	
url='https://api.bilibili.com/x/relation/stat?vmid=%d&jsonp=jsonp'
url2='http://api.bilibili.com/x/web-interface/archive/stat?aid=65930235'
#t=get_json(url)
#print(t['data'])
#print(t['data']['follower'])
#print(t['data']['following'])
def main(mid=34625132):
	t=get_json(url % mid)
	print('这位UP主有%d位粉丝，ta关注有%d位UP主' % (t['data']['follower'],t['data']['following']))
	print(t['data'])
	
main(int(input('请输入要查询的mid:')))