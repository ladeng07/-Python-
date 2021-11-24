import pandas as pd
import collections
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

ex=pd.read_excel('2019年12月学业水平考试2018级考生成绩.xls')
print(ex.iloc[0,5:10])
class_list=[1,70,137,205,270,328,395,464,535,592,660,728,796,864,934,1004,1075,1126,1196,1263,1333]
class_list=[i-1 for i in class_list]

l=[list([list(ex.iloc[i,5:10]) for i in range(class_list[e],class_list[e+1]) if e < 20]) for e in range(0,20)]
s=sum([len(i) for i in l])
print(s)
print(l[-1][-1][0])

wl=[(len([e[3] for e in i if e[3] =='A']),len(i)) for i in l]  #选择科目 0 -物理
print(wl)


matplotlib.rcParams['font.sans-serif']=['SimHei']   
matplotlib.rcParams['axes.unicode_minus']=False
#plt.ylim(0,900)

def al(rects):
	n=0
	color='grby'
	for e,i in enumerate(rects):
		plt.text(i.get_x()+i.get_width()/2,i.get_height()*1.03,i.get_height(),ha='center',va='bottom',fontsize='large',color=color[e])
		


tag=['优秀','不优秀']
name=['%d班'%i for i in range(1,21)]
print(tag)
for e in range(0,20):
        c=wl[e]
        x=np.linspace(0,len(c),len(c))
        v=(c[0],c[1]-c[0])
        print(v)
        print(x)
        name_list=['%d班'%i for i in range(1,21)]
        plt.subplot(4,5,1+e)
        plt.ylim(0,80)
        plt.ylabel('人数')
        plt.xlabel(name[e]+'\n\n\n\n\n\n\n ',fontsize='x-large',verticalalignment='bottom')
        #plt.title('2\n\n'+name[e],fontsize='large')
        al(plt.bar(x,v,color='grby',tick_label=tag))


plt.show()
