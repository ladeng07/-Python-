import requests
import time
import json
url='https://lab.isaaclin.cn/nCoV/api/overall'
url2='https://lab.isaaclin.cn/nCoV/api/area?latest=1&province='
def get_json(url):
	res=requests.get(url)
	js=json.loads(res.text)
	return js
	
def get_time(sec):
	t=time.localtime((sec/1000))
	return t[:5]

def get_info(r):
	return (r['confirmedCount'],
	r['currentConfirmedCount'],
	r['suspectedCount'],
	r['curedCount'],
	r['deadCount'])

def get_p(de):
	j=get_json(url2+str(de))
	if j['results'] == []:
		print('哎呀，你输入的地址有误啊，再输一遍吧')
	else:
		r=j['results'][0]
		t=get_time(r['updateTime'])
		print('截止至%d年%d月%d日%d时%d分时许，\n%s累计确诊病例%d例,现有确诊%d例，现有疑似患者%d例，\n累计治愈出院%d例，累计死亡病例%d例。\n#######################' % (t+(r['provinceName'],)+get_info(r)))
		a=input('是否查看下辖区详细情况？Y/N: ')
		if a == 'Y' or a == 'y' and r['cities'] != []:
			for i in r['cities']:
				print('%s累计确诊病例%d例,现有确诊%d例，现有疑似患者%d例，\n累计治愈出院%d例，累计死亡病例%d例。\n====================================' % ((i['cityName']+'市',)+get_info(i)))
		elif a=='n' or a=='N':
			return 
		print('抱歉，该省份暂不支持查看下辖区情况。')

	
def main():
	j=get_json(url)
	r=j['results'][0]
	t=get_time(r['updateTime'])
	print('截止至%d年%d月%d日%d时%d分时许，\n我国累计确诊病例%d例，较昨日新增%d例,\n现有确诊%d例，现有疑似患者%d例，较昨日新增%d例，\n累计治愈出院%d例，较昨日新增%d例,\n现有重症%d例,累计死亡病例%d例,较昨日新增%d例。\n$$$$$$$$$$$$$$$$$$$$$$$$$$' % (t[:5]+(
	r['confirmedCount'],
	r['confirmedIncr'],
	r['currentConfirmedCount'],
	r['suspectedCount'],
	r['suspectedIncr'],
	r['curedCount'],
	r['curedIncr'],
	 r['seriousCount'],
	r['deadCount'],
	r['deadIncr'])))
	
	while 1:
		de=input('请输入要查看的省份(一定要全称,例如"湖北省"): ')
		get_p(de)
main()
