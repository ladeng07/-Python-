import math
n=int(input())
def son(num):
	i=2
	while i <= num:
		if num%i == 0:
			print(i)
			son(num/i)
			break
		i+=1
			

son(n)	

	
