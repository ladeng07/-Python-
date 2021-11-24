from itertools import combinations
n=0
m=0
l=list(combinations([1,2,3,4,5],3))
l1=list(combinations([1,2,3,4,5],2))
l2=list(combinations([1,2,3,4,5],1))
for i in l:
	for e in l:
		for h in l:
			if len(set(i+e+h)) == 5:
				n+=1
				print(n)
				print(i,e,h)
				
for i in l:
	for e in l:
		for h in l1:
			if len(set(i+e+h)) == 5:
				m+=1
				print(m)
				print(i,e,h)
n += 3*m
m=0				
				
for i in l:
	for e in l1:
		for h in l1:
			if len(set(i+e+h)) == 5:
				m+=1
				print(m)
				print(i,e,h)
n += 3*m
m=0
				
for i in l1:
	for e in l1:
		for h in l1:
			if len(set(i+e+h)) == 5:
				n+=1
				print(n)
				print(i,e,h)
				
for i in l:
	for e in l1:
		for h in l2:
			if len(set(i+e+h)) == 5:
				m+=1
				print(m)
				print(i,e,h)
				
n += 6*m
print(n)
m=0

for i in l:
	for e in l:
		for h in l2:
			if len(set(i+e+h)) == 5:
				m+=1
				print(m)
				print(i,e,h)

n += 3*m
print(n)
m=0				

for i in l:
	for e in l2:
		for h in l2:
			if len(set(i+e+h)) == 5:
				m+=1
				print(m)
				print(i,e,h)
				
n += 3*m
print(n)
m=0

for i in l1:
	for e in l1:
		for h in l2:
			if len(set(i+e+h)) == 5:
				m+=1
				print(m)
				print(i,e,h)
n += 3*m
print(n)
m=0

		