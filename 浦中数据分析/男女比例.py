import pandas as pd
import collections
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

ex=pd.read_excel('2019年12月学业水平考试2018级考生成绩.xls')
print(ex.iloc[0,5:10])
class_list=[2,70,137,205,270,328,395,464,535,592,660,728,796,864,934,1004,1075,1126,1196,1263,1333]
class_list=[i-1 for i in class_list]

l=[list([list(ex.iloc[i,5:10]) for i in range(class_list[e],class_list[e+1]) if e < 20]) for e in range(0,20)]
s=sum([len(i) for i in l])
print(s)
print(l[-1][-1][0])

wl=[(len([e[4] for e in i if e[4] =='A']),len(i)) for i in l]  #选择科目 0 -物理
print(wl)

boy=0
girl=0
boy_all=0
e=5
for i in range(1,1332):
        num=int(ex.iloc[i,4][-2]) % 2
        if num==1:
                boy_all += 1
                if ex.iloc[i,e] == 'A':
                        boy += 1
        elif num == 0:
                if ex.iloc[i,e] == 'A':
                        girl += 1
print(boy,girl,boy_all)

matplotlib.rcParams['font.sans-serif']=['SimHei']   
matplotlib.rcParams['axes.unicode_minus']=False
#plt.ylim(0,900)

def al(rects):
	n=0
	color='grby'
	for e,i in enumerate(rects):
		plt.text(i.get_x()+i.get_width()/2,i.get_height()*1.03,i.get_height(),ha='center',va='bottom',fontsize='large',color=color[e])
		


tag=['男生','女生']
name=['%d班'%i for i in range(1,21)]
print(tag)
c=(boy_all,1331-boy_all)
plt.ylim(0,920)
plt.title('高二男女比例')
x=np.linspace(0,len(c),len(c))
al(plt.bar(x,c,color=['mediumblue','pink'],tick_label=tag))



plt.show()
