import pandas as pd
import collections
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

ex=pd.read_excel('2019年12月学业水平考试2018级考生成绩.xls')
print(ex.iloc[0,5:10])

matplotlib.rcParams['font.sans-serif']=['SimHei']   
matplotlib.rcParams['axes.unicode_minus']=False
#plt.ylim(0,900)

def al(rects):
	n=0
	for i in rects:
		plt.text(i.get_x()+i.get_width()/2,i.get_height()*1.03,i.get_height(),ha='center',va='bottom',fontsize='large')


tag=list(ex.iloc[0,5:10])
print(tag)
color='rgby'

#c=collections.Counter([ex.iloc[i,4][6:14] for i in range(1,1332)])
c=collections.Counter([ex.iloc[i,4][10:14] for i in range(1,1332)]).most_common(50)
name_list=['%d月%d日' % (int(i[0])//100,int(i[0])%100) for i in c]
c=[i[1] for i in c]
print(c)
print(len(c))
print(name_list)
plt.ylim(0,20)
plt.title('浦中高二生日月份分布',fontsize='x-large')
#name_list=['%d月'%i for i in range(1,13)]
x=np.linspace(0,len(c),len(c))
al(plt.bar(x,c,color=['red','green','blue','yellow','pink','lime','royalblue']))
plt.xticks(x,name_list,rotation=45)
plt.yticks(np.linspace(0,20,21))


plt.show()
