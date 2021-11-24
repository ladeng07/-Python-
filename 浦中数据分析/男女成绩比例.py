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
		plt.text(i.get_x()+i.get_width()/2,i.get_height()*1.03,'%.2f' % i.get_height()+'%',ha='center',va='bottom',fontsize='large')


tag=list(ex.iloc[0,5:10])
print(tag)
color='rgby'



name_list=['男生','女生']
for e in range(0,5):
        boy=0
        girl=0
        boy_all=0
        for i in range(1,1332):
                num=int(ex.iloc[i,4][-2]) % 2
                if num==1:
                        boy_all += 1
                        if ex.iloc[i,e+5] == 'A':
                                boy += 1
                elif num == 0:
                        if ex.iloc[i,e+5] == 'A':
                                girl += 1
        print(boy,boy_all-boy,girl,1331-boy_all-girl)
        a,b,c,d=num=[boy,boy_all-boy,girl,1331-boy_all-girl]
        kf=(sum(num)*(a*d-b*c)**2)/((a+b)*(a+c)*(b+c)*(c+d))
        print(kf)
        x=np.linspace(0,2,2)
        v=(round(boy/boy_all*100,2),round(boy/(1331-boy_all)*100,2))
        plt.subplot(231+e)
        plt.ylim(0,100)
        #plt.xlabel(tag[e]+'\n\n\n\n\n',verticalalignment='bottom')
        plt.ylabel('优秀率')
        plt.title(tag[e],fontsize='x-large')
        al(plt.bar(x,v,color=['b','pink'],tick_label=name_list))


plt.show()
