def tf(num):
	if num>3:
		for i in range(3,num+1):
			#print(l)
			s=num-i
			print('s',s)
			if s< i:
				for n in range(0,int(s/2)+1):
					if (s-n)<(i/2)  and int(i-2*(s-n)) !=1 and int(i-2*(s-n))%2==1:
						for m in range(0,(int(i-2*(s-n))+1)//2):
							print('j',int(i-2*(s-n)))
							l=[[0]  for i in range(1,i+1)]
							l[s-n+m].extend((s-n,-n))
							print(l)
							print('额',)
					elif (s-n)<(i/2)  and int(i-2*(s-n))==1:
						for m in range(0,int(i-2*(s-n))):
							print('j',int(i/2-(s-n))+1)
							l=[[0]  for i in range(1,i+1)]
							l[s-n+m].extend((s-n,-n))
							print('小强')
							print(l)
					else:
						print('龙一光牛逼')
			#print(i)
	else:
		print('没太有同分异构体，')
	
tf(10)