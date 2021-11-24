def feb(n):
	a,b = 0,1
	while b<n:
		yield b
		a,b=b,a+b
l=[i for i in range(2,1000) if 0 not in [i%each for each in range(2,int(i**0.5)+1)]]
l=[i for i in feb(1000) if i in l]
print(l)