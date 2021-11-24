string='bebb'
def fc337(string):
	print({[string[n] for n,e in enumerate(str(bin(i))[2:]) if e=='1'] for i in range(1,2**len(string)+1)})




fc337(string)