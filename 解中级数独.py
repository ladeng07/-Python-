def line(l,num):#判断行的数字符不符合
	return list([i for i in range(1,10) if i not in l[num]])

def column(l,num,num_l):#判断列的数字符不符合
	return list([e for e in num_l if e not in [i[num] for i in l]])
	
def kuai(l,x,y,num_l):#判断九宫格的数字符不符合
	if x<3 and y<3:
		return list([i for i in num_l if i not in [e for i in l[:3] for e in i[:3]]])
	elif 2<x<6 and y<3:
		return list([i for i in num_l if i not in [e for i in l[:3] for e in i[3:6]]])
	elif 5<x and y<3:
		return list([i for i in num_l if i not in [e for i in l[:3] for e in i[6:]]])
	elif x<3 and 2<y<6:
		return list([i for i in num_l if i not in [e for i in l[3:6] for e in i[:3]]])
	elif 2<x<6 and 2<y<6:
		return list([i for i in num_l if i not in [e for i in l[3:6] for e in i[3:6]]])
	elif 5<x and 2<y<6:
		return list([i for i in num_l if i not in [e for i in l[3:6] for e in i[6:]]])
	elif x<3 and 5<y:
		return list([i for i in num_l if i not in [e for i in l[6:] for e in i[:3]]])
	elif 2<x<6 and 5<y:
		return list([i for i in num_l if i not in [e for i in l[6:] for e in i[3:6]]])
	elif 5<x and 5<y:
		return list([i for i in num_l if i not in [e for i in l[6:] for e in i[6:]]])
				
def r2(l,r):#穷举所有有两个数字格子
	li=[]
	for y in range(0,9):
		for x in range(0,9):
			if l[y][x]==0:
				result=kuai(l,x,y,column(l,x,line(l,y)))
				if len(result) ==2:
					li.append((x,y,result))
	for n,i in enumerate(li):
		l[i[1]].insert(i[0],i[2][r[n]])
		del l[i[1]][i[0]+1]
	return l
		
def shudu(l):#解数独的主要程序
	test=list([list([e for e in i]) for i in l])
	n=1
	while n==1 or test!=l :
		for y in range(0,9):
			for x in range(0,9):
				if l[y][x]==0:
					result=kuai(l,x,y,column(l,x,line(l,y)))
					if len(result) ==1:
						l[y].insert(x,result[0])
						del l[y][x+1]
					elif result==[]:
						return l,'ok'
		n=0
		if l==test:
			m=0
			for y in range(0,9):
				for x in range(0,9):
					if l[y][x]==0:
						result=kuai(l,x,y,column(l,x,line(l,y)))
						if len(result)==2:
							m+=1
			return l,m
		return shudu(l)
		
def main(l):
	m=1
	i=0
	l,n=shudu(l)
	print(l)
	test=list([list([e for e in i]) for i in l])
	while list([e for i in l for e in i if e==0])!=[]:
		for i in range(0,2**n):
			string=str(bin(i)[2:])
			if len(string) <n:
				string='0'*(n-len(string)+1)+string
			l=r2(l,list([int(i) for i in string]))
			l,x=shudu(l)
			if list([e for i in l for e in i if e==0])==[]:
				#数据修正部分，我也不知道为什么，总会有一个重复。
				for y,g in enumerate(l):
					if len(set(g))!=len(g):
						for x,n in enumerate(g):
							if g.count(n) ==2:
								for e in range(1,10):
									if e not in g:
										l[y].insert(x,e)
										del l[y][x+1]
								
				break
			print('第%d次尝试,失败。( ´◔ ‸◔`)' % (i+1))
			l=list([list([e for e in i]) for i in test])
	print('第%d次尝试，成功了。ヽ(๑Θ｡Θ๑)ﾉ' % (i+1))
	for i in l:
		print(i)
		
shudu1 = ['902547360',"465003027","730926805","006815479","809364502","514070083","157098206","240601090","098730154"]
shudu2 = ["000056810","070000000","800010300","040009003","000080000","190000048","015008002","069270405","200540600"]
shudu3=['000750000','030048020','100000006','040000008','790000031','200000070','500000007','080320040','000069000']#24个数，
shudu4=[[0,0,8,0,0,0,2,0,0],
[0,3,0,8,0,2,0,6,0],
[7,0,0,0,9,0,0,0,5],
[0,5,0,0,0,0,0,1,0],
[0,0,4,0,0,0,6,0,0],
[0,2,0,0,0,0,0,7,0],
[4,0,0,0,8,0,0,0,6],
[0,7,0,1,0,3,0,9,0],
[0,0,1,0,0,0,8,0,0]]
l=list([list([int(e) for e in i]) for i in shudu3])
main(l)
#main(shudu4)