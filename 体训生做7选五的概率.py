import itertools
n=0
def fx(l):
	n=0
	for e,i in enumerate(l):
		if i == e+1:
			n += 1
	if n == 2:
		return True
	else:
		return False

for i in list(itertools.permutations([1,2,3,4,5,6,7],5)):
	if fx(i):
		print(i)
		n += 1
print(n)