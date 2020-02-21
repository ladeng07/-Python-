import tkinter as tk
import webbrowser
import collections
'''def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
root = tk.Tk ()
s1 = tk.Scrollbar(root)
s1.pack(side='right',fill='y')

photo = tk.PhotoImage(file='F:\\a.gif')

l = tk.Listbox(root,selectmode='extended',yscrollcommand=s1.set)
l.pack()
for each in range(1,110):
       l.insert('end',each)
b = tk.Button(root,text='hit-me',\
              command=lambda x=l:x.delete('active'))
b.pack()
s1.config(command=l.yview)
sc = tk.Scale(root,from_=0,to=42)
sc.pack()
def show():
    print(sc.get())
    l.insert('end',sc.get())
b1 = tk.Button(root,text='get-me',\
              command=show)
b1.pack()

txt = tk.Text(root,width='200',height='10')
txt.pack()
txt.insert('insert','哈哈哈哈哈，暴打龙一光')
txt.insert('insert','哈哈哈哈哈，暴打龙一光')
txt.insert('insert','哈哈哈哈哈，暴打龙一光')
 
def p ():
    txt.image_create('end',image=photo)
    print(txt.get('1.2',1.6))
b2 = tk.Button(root,text='get-me',\
              command=p)
txt.window_create('insert',window=b2)

txt.tag_add('tag1','1.7','1.9','1.15')
txt.tag_config('tag1',background='yellow',foreground='red',underline=True,spacing1=10)
def show_arrow_cursor(event):
    txt.config(cursor='arrow')
def show_xterm_cursor(event):
    txt.config(cursor='xterm')
def click(event):
    webbrowser.open('www.baidu.com')

txt.tag_bind('tag1','<Enter>',show_arrow_cursor)
txt.tag_bind('tag1','<Leave>',show_xterm_cursor)
txt.tag_bind('tag1','<Button-1>',click)

tk.mainloop()'''

import itertools
def fun107(lst):
    new=[]
    for k,g in itertools.groupby(lst):
        l = len(list(g))
        if l >1:
            print(l)
            new.extend([k,l])
        else:
            new.append(k)
    print(new)


def fun108(score):
        d = {10:'满分，牛逼', 9:'优秀！', 8:'良好！', 7:'中等！', 6:'及格！'}
        print(d.get(score//10,'不及格。。。。'))


lst = [12, 1, 3, 19, 0, 1, 16, 8, 19, 10, 6, 10, 0, 4, 3, 18, 2, 18, 17, 6, 16, 19, 12, 18, 4, 4, 16, 12, 13, 11, 0, 0, 12, 7, 10, 2, 7, 12, 4, 18, 13, 18, 16, 17, 14, 12, 1, 12, 4, 14, 8, 18, 4, 12, 10, 1, 18, 7, 2, 9, 3, 11, 12, 2, 9, 13, 12, 18, 15, 1, 9, 5, 11, 6, 12, 9, 16, 14, 18, 0, 15, 4, 17, 5, 1, 13, 0, 10, 0, 6, 16, 15, 3, 16, 20, 18, 4, 18, 16, 3]
def fun133(lst):
	return [[i,lst.count(i)] for i in set(sorted(lst))]
print(list(fun133(lst)))

l = [1,2,3,5,6,7,9,0]
def fun131(lst):
	return [i for i in range(min(lst),max(lst)+1) if i not in lst]
print(list(fun131(l)))

def fun127():
	return [s for s in [str(i*i) for i in range(3163,10000) if len(set(str(i*i))) == 8] if sum(map(int,s[0::2])) == sum(map(int,s[1::2]))]	
print(fun127())
l1 = [2, 10, -3, 9, 4, 3, 5, 7 ,12]
def fun126(mylist,target):
	l = [[mylist[i],each]for i in range(len(mylist)) for each in mylist[i+1:] if mylist[i] + each==target]
	return l if len(l) != 1 else sum(l,[p])
print(fun126(l1,9))

def fun187(num):
    count = num
    for each in range(1,10):
        if num / each == int(num / each) and num / each > 0:
            if abs(each - num) / each < count:
                count = abs(each - num / each)
                num1 = each
                num2 = num / each
    print ('最小的一组乘积为%d * %d' % (num1,num2))
            
import math
def fun186 (num_list):
    l2 = []
    global lenght,frist_list,l
    if int(num_list[-1]) < 10:
        l = []
        lenght = len(num_list)
        for num in num_list:
            if int(math.sqrt(int(num))) == math.sqrt(int(num)):
                l.append(num)
        frist_list = num_list
        num_list = range(lenght)
    elif lenght == len(str(num_list[-1])):
        return print(sorted(set(l)))
    for each in num_list:
        for i in range(lenght):
            if str(i) not in str(each):
                nums =int(str(each) + str(i))
                l2.append(nums)
                number = ''
                for n in str(nums):
                    number += str(frist_list[int(n)])
                if math.sqrt(int(number)) == int(math.sqrt(int(number))):
                    l.append(int(number))
    fun186(l2)

def fun189(nums):
    result = float('%.2f' % (sum(nums) / len(nums)))
    l1 = [abs(each - result) for each in nums]
    ind = l1.index(sorted(l1[:])[0])
    if sorted(l1[:])[0] != sorted(l1[:])[1]:
        return (nums[ind],)
    elif nums.count(nums[ind]) > 1:
        return (nums[ind],)
    else:
        return (nums[ind],nums[l1.index(sorted(l1[:])[0],ind+1)])

def fun192(num_list):
	l = []
	for i,each in enumerate(num_list):
		if each < len(num_list) - 1:
			num = num_list[each+1]
			if abs(i) - abs(num) > 1:
				l.append(i)
				if i > num:
					while i > num:
						i -= 1
						l.append(i)
	print(l)					
						
fun192([4,2])

def fun195(dicts,key):
	try:
		fun195(dicts,dicts[key])
	except KeyError:
		print(dicts[key])
	except RuntimeError:
		return None
fun195({'A':'B','B':'C'},'A')

def fun198(t):return print(eval(t))
fun198(input('请输入一条算式>>>'))


import numpy as np
def fun199(l):
    w = len(l)
    x = np.array(l)
    x = np.sort(l, axis=None)
    x.shape = w,w
    x.tolist()
    for i in range(w):
        for each in range(w):
            if i + 2 % 2 == 0:
                l[each][i]= x[i][each]
            else:
                l[each][i]= x[i][::-1][each]
    return l
fun199([[-15, -82, 88, -10], [-29, -88, -43, 23], [-2, 27, 26, 8], [64, 39, 65, 93]])


def fun200(string):
    print(string.swapcase().translate(string.maketrans('123456789','987654321')).replace('0','10'))

a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
d = zip(a,b,c)
def fun201(*args):
    lenth = 0
    for i in args:
        if len(i) > lenth:
            lenth = len(i)
    l = []
    for i in range(lenth):
        t = []
        for each in args:
            try:
                t.append(each[i])
            except  IndexError:
                t.append(None)
        l.append(tuple(t))
    return l
str1 = 'ABC'
list1 = [1, 2, 3,[4, 5]]
tuple1 = (1.1, 2.2)
print(fun201(str1, list1, tuple1))

import random
def fun202():
    l = []
    for i in range(4):
        num =random.randint(5,9)
        l.append(num)
    while len(l) < 8:
        num = random.randint(0,9)
        if sum(l)+num <= 40 and len(l) < 8:
            if 40 - sum(l) > num and 40 - sum(l) < (7-len(l))*9+num:
                l.append(num)
                random.shuffle(l)
        else:
            l.append(40-sum(l))
    return l 

def fun203(n):
    m = n
    while n > 1:
        m = (n-1)+1/m
        n -= 1
    return m

def strrange (start,end=None,step=1):
    #fun204
    if end==None:
        end=start
        start='A'
    l=[chr(i) for i in range(65,123) if chr(i).isalpha()]
    print(''.join(l[l.index(start):l.index(end):step]))

def fc333(string):
	for each in sorted(set(string.upper()))[::-1]:
		if each in string and each.lower() in string:
			return print(each)
	print('~')
	
	
string='abaaaa'
def fc334(string):
	l=string.split('aaa')
	l2=[]
	for i in l:
		l2.extend(i.split('bbb'))
	ma=len(max(l2))
	if len(l2)==1:
		print(ma)
	elif l2[0]==max(l2) or l2[len(l2)-1] == max(l2):
		print(ma+2)
	else:
		print(ma+4)
fc334(string)



def fc335(paragraph,banned):
        return collections.Counter([i.strip('!?\',;.') for i in paragraph.lower().split() if i.strip('!?\',;.') not in banned]).most_common(1)[0][0]
        
        
m=3
woods=[2,10]
def fc336(m,woods):
	for i in range(max(woods),0,-1):
		if m<=woods.count(i):
			return i
		elif m <= len([h for e in sorted(woods)[::-1] if e//i != 0 or e==i for h in [i]*(e//i)]):
			return i
	return 0
fc336(m,woods)
		