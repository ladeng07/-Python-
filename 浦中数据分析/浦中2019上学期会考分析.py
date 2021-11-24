import pandas as pd
import collections
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

ex=pd.read_excel('2019年12月学业水平考试2018级考生成绩.xls')
print(ex.iloc[0,5:10])

'''matplotlib.rcParams['font.sans-serif']=['SimHei']   
matplotlib.rcParams['axes.unicode_minus']=False
#plt.ylim(0,900)

def al(rects):
	n=0
	for i in rects:
		plt.text(i.get_x()+i.get_width()/2,i.get_height()*1.03,i.get_height(),ha='center',va='bottom',fontsize='large')


tag=list(ex.iloc[0,5:10])
print(tag)
color='rgby'
for e in range(0,5):
        c=sorted(collections.Counter([i for i in ex.iloc[1:,5+e]]).most_common())
        x=np.linspace(0,len(c),len(c))
        v=[i[1] for i in c]
        name_list=[i[0] for i in c]
        plt.subplot(231+e)
        plt.ylim(0,900)
        #plt.xlabel('分数')
        plt.ylabel('人数')
        plt.title(tag[e],fontsize='large')
        al(plt.bar(x,v,color='grby',tick_label=name_list))


plt.show()'''
