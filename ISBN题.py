string=input()
str1=string.split('-')
str1=''.join(str1)
end_num=sum([int(i)*(n+1) for n,i in enumerate(str1[:-1])])%11

if end_num == 10 and str1[-1] == 'X':
	print('Right')
elif end_num == 10 and str1[-1] != 'X':
	print(string[:-1]+'X')
elif end_num != 10 and str1[-1] == 'X':
	print(string[:-1]+str(end_num))
elif end_num < 10 and end_num == int(str1[-1]):
	print('Right')
else:
	print(string[:-1]+str(end_num))