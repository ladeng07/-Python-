def gcd(x,y):
	while y:
		t=y%x
		x=y
		y=t
	print(x)
gcd(200,10)