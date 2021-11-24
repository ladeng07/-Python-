n,t1,t2=input()
a=input()
b=input()

def guess_fist(a,b):
	if a==b:
		return 0
	elif a == 0 and a != b:
		if b == 2 or b == 3:
			return 1
		else:
			return -1
	elif a == 1 and a != b:
		if b == 0 or b == 3:
			return 1
		else:
			return -1