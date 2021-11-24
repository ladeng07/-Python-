import pandas as pd
import collections
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

ex=pd.read_excel('2019年12月学业水平考试2018级考生成绩.xls')
print(ex.iloc[0,5:10])
class_list=[1,70,137,205,270,328,395,464,535,592,660,728,796,864,934,1004,1075,1126,1196,1263,1332]
class_list=[i for i in class_list]

l=[list([int(ex.iloc[i,4][-2])% 2 for i in range(class_list[e],class_list[e+1]) if e < 20]) for e in range(0,20)]
s=sum([len(i) for i in l])
print(len(l[8]))
l=[sorted(collections.Counter(i).most_common()) for i in l]
l=[(i[0][1],i[1][1]) for i in l]
print(l)
l=[round(i[0]/sum(i)*100,2)for i in l]
print(l)


matplotlib.rcParams['font.sans-serif']=['SimHei']   
matplotlib.rcParams['axes.unicode_minus']=False
#plt.ylim(0,900)

def al(rects):
	for e,i in enumerate(rects):
		plt.text(i.get_x()+i.get_width()/2,i.get_height()*1.03,'%.2f' % i.get_height()+'%',ha='center',va='bottom',fontsize='large')
		


name=['%d班'%i for i in range(1,21)]
for e in range(0,20):
        x=np.linspace(0,len(l),len(l))
        name_list=['%d班'%i for i in range(1,21)]
        plt.ylim(0,120)
        plt.ylabel('女生比例')
        #plt.xlabel(name[e]+'\n\n\n\n\n\n\n ',fontsize='x-large',verticalalignment='bottom')
        plt.title('高二各班男女比例图',fontsize='x-large')
        al(plt.bar(x,l,color=['red','g','b','yellow','pink','lime','royalblue'],tick_label=name_list))


plt.show()
