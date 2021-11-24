n=int(input())
man_list=[]
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
m=1
for i in range(n):
	man=input().split()
	if man == []:
		man=input().split()
	#print(man)
	if man[1] != 'BangZhu' and man[1] != 'FuBangZhu':
		#print(man[1])
		man_list.append(man) 



man_list=sorted(man_list,key=lambda x : int(x[2]),reverse=True)

for i in man_list:
	print(i)
	if m < 3:
		l1.append(i)
		m += 1
	elif m < 7:
		l2.append(i)
		m += 1
	elif  m < 14:
		l3.append(i)
		m += 1
	elif m < 39:
		l4.append(i)
		m += 1
	else:
		l5.append(i)
		
