
n='2c'
print(eval('0x'+n))

def k1(n):
	a=int(eval('0x'+n[0]))
	b=int(eval('0x'+n[1]))
	if b%2==0:
		return str('{:02x}'.format((a*16+b)^30))
	else:
		if 5 <b:
			y=(b-6)^6
		elif b<6:
			y=(b+10)^6
		return str('{:02x}'.format((a^1)*16+y))
		
print(k1(n))

n='84'
def k2(n):
	a=int(eval('0x'+n[0]))
	b=int(eval('0x'+n[1]))
	if 7 < b < 16:
		a = (a+1)%16
	if a <5:
		y=4-a
	elif a>4:
		y=20-a
	return str('{:02x}'.format(y*16+b^1))
	
print(k2(n))

n='2c'
def k3(n):
	a=int(eval('0x'+n[0]))
	b=int(eval('0x'+n[1]))
	if 7 < b:
		a = (a+1)%16
	if a <9:
		y=(a+7)^13
	elif a>8:
		y=(a-9)^13
	return str('{:02x}'.format(y*16+b^7))
	
print(k3(n))

n='1c'
def k4(n):
	a=int(eval('0x'+n[0]))
	b=int(eval('0x'+n[1]))
	if b>13:
		a = (a+1)%16
	if 1<a:
		y=(a-2)^11
	else:
		y=(a+14)^11
		
	if b<5:
		x=(4-b)^13
	elif b >4:
		x=(20-b)^13
	return str('{:02x}'.format(y*16+x))
	
print(k4(n))

n='32'
def k5(n):
	a=int(eval('0x'+n[0]))
	b=int(eval('0x'+n[1]))
	if 11 < b:
		a = (a+1)%16
		
	if b < 4:
		y=(b+12)^3
	elif 3<b:
		y=(b-4)^3
	return str('{:02x}'.format((a^12)*16+y))
	
print(k5(n))

n='80'
def k6(n):
	a=int(eval('0x'+n[0]))
	b=int(eval('0x'+n[1]))
	if (279-a*16-b-(b^7))//16%2==1:
		y=(247-a*16-b-(b^7))//16
	else:
		y=(471-a*16-b-(b^7))//16%16
		
	return str('{:02x}'.format(y*16+b^7)
	)
	
print(k6(n))

def key(n):
	print(k1(n[0:2]),end='  ')
	print(k2(n[2:4]),end='  ')
	print(k3(n[4:6]),end='  ')
	print(k4(n[6:8]),end='  ')
	print(k5(n[0:2]),end='  ')
	print(k6(n[2:4]))
	
n='3ED0220E'
l='DC08195B'
m='7bcd332e'
l=input('输入 : ')
key(l)