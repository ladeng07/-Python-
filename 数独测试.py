def line(l,num):
	return list([i for i in range(1,10) if i not in l[num]])

def column(l,num,num_l):
	return list([e for e in num_l if e not in [i[num] for i in l]])
	
def kuai(l,x,y,num_l):
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
		
		
def shudu(l):
	test=list([list([e for e in i]) for i in l])
	n=1
	old_l=l
	#print(test)
	while n==1 or test!=l :
		print('hh')
		for y in range(0,9):
			for x in range(0,9):
				if l[y][x]==0:
					result=kuai(l,x,y,column(l,x,line(l,y)))
					#print(result)
					if len(result) ==1:
						#print(result)
						#print(l[y][x])
						l[y].insert(x,result[0])
						del l[y][x+1]
						#print(test)
					elif result==[]:
						print('ko')
						return l,'ok'
		print(l)
		n=0
		if l==test:
			m=0
			for y in range(0,9):
				for x in range(0,9):
					if l[y][x]==0:
						result=kuai(l,x,y,column(l,x,line(l,y)))
						if len(result)==2:
							print(result)
							m+=1
			print(m)
			return l,m
		return shudu(l)
	

shudu2 = ["000056810","070000000","800010300","040009003","000080000","190000048","015008002","069270405","200540600"]
l=list([list([int(e) for e in i]) for i in shudu2])
global old_l
shudu(l)