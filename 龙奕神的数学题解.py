n=0
def cz(li):
	l=[[],[],[]]
	for i in range(0,5):
		if li[i] == 65:
			l[0].append(i+1)
		elif li[i] == 66:
			l[1].append(i+1)
		else:
			l[2].append(i+1)
	l=[str(i).strip('[]') for i in l]
	l2=list('甲乙丙')
	return dict(zip(l2,l))
for j in range(65,68):
	for k in range(65,68):
		for l in range(65,68):
			for i in range(65,68):
				for e in range(65,68):
					li=[j,k,l,i,e]
					if li.count(66) < 4 and li.count(65) < 4 and li.count(67) < 4 and len(set(li)) == 3 :
						n+=1
						print('第%d种可能' % n)
						x=cz(li)
						print('甲去%(甲)s号村庄，乙去%(乙)s号村庄,丙去%(丙)s号村庄' % x)
						#li=[chr(i) for i in li]
						#print(li)