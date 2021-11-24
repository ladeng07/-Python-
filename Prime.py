'''def Fun (n,m):
    if m == 0:
        return 1
    else:
        result = n**m + Fun (n,m-1)
        return result
n = int(input('请输入一个整数：'))
m = int(input('请输入幂：'))
print(Fun (n,m))
def fun198(t):return print(eval(t))
fun198(input('请输入一条算式>>>'))
import time

def p(n):
    l = [i for i in range(2,n+1) if i==2 or (i >2 and i%2!=0)]
    for i in range(3,n,2):
        if i in l:
            rm = [i for i in range(2*i,n,i) if i in l]
            for i in rm:
                l.remove(i)
    return l

def Prime(n):
    return [i for i in range(2,n+1) if 0 not in [i%j for j in range(2,int(i**0.5)+1)]]
while 1:
    n = int(input(':'))
    s = time.time()
    #Prime(n)
    p(n)
    e = time.time()
    print('time:%s' % str(e-s))'''
