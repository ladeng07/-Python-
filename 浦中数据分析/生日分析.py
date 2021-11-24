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
print(sorted(collections.Counter([ex.iloc[i,4][10:14] for i in range(1,1332)]).most_common()))
c=sorted(collections.Counter([ex.iloc[i,4][10:12] for i in range(1,1332)]).most_common())
c=[i[1] for i in c]
print(c)
print(len(c))
plt.ylim(0,160)
plt.title('浦中高二生日月份分布',fontsize='x-large')
name_list=['%d月'%i for i in range(1,13)]
x=np.linspace(0,len(c),len(c))
al(plt.bar(x,c,color='r',tick_label=name_list))


plt.show()
