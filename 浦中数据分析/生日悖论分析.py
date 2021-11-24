import pandas as pd
import collections
import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

ex=pd.read_excel('2019年12月学业水平考试2018级考生成绩.xls')
print(ex.iloc[0,5:10])

matplotlib.rcParams['font.sans-serif']=['SimHei']   
matplotlib.rcParams['axes.unicode_minus']=False


c=[ex.iloc[i,4][10:14] for i in range(0,1332)]
def jc(n):
        if n == 1:
                return 365   #用递归计算365*364*....*366-n的积
        return jc(n-1)*(366-n)


def fun(n):
       return round(1-jc(n)/365**n,4)   #计算n个人中至少两人生日相同的概率


def birthday(n):
        count=0
        for i in range(10000):
                num=[]
                while 1:
                        r=random.randint(0,1331) #获取含有n个随机数的列表
                        if len(num) == n:
                                break
                        if r not in num:
                                num.append(r)

                num=[c[i] for i in num]
                if len(num) != len(set(num)):  #计算10000此中，至少有两人生日相同的结果
                        count += 1

        print('n=%d -- 概率为%f' %(n,count/10000))
        return round(count/10000,4)


y1=[birthday(i) for i in range(10,51)] #从1331人中每次抽n人,进行10000次得出的测量数据

y2=[fun(i) for i in range(10,51)] #通过公式得出的概率精确值

yp=sum(y1)/len(y1)
r=sum([(i-y2[n])**2 for n,i in enumerate(y1)])/sum([(i-yp)**2 for i in y1])  #相关指数R^2的计算
print('相关指数',1-r)
        
x=np.linspace(10,len(y1)+9,len(y1))
plt.plot(x,y1,color='r',label='测量数据')
plt.plot(x,y2,color='b',label='回归曲线')
plt.title('生日悖论的回归曲线拟合数据')    # 画图
plt.xlabel('人数 n')
plt.ylabel('概率 P')
plt.ylim(0,1)
plt.legend()
plt.grid() 
plt.show()
