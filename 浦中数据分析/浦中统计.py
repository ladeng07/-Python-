import pandas as pd
import collections
import wordcloud
import matplotlib
import matplotlib.pyplot as plt
import PIL.Image as image
import numpy as np
ex=pd.read_excel('浦北中学各班同学线上补习账号及密码（高二）.xlsx')
name=list([i[:len(i)-2] if len(i)>2 else i[0]  for i in ex['姓名']])
matplotlib.rcParams['font.sans-serif']=['SimHei']   
matplotlib.rcParams['axes.unicode_minus']=False
l=collections.Counter(name).most_common(20)
print(l)





def al(rects):
	n=0
	for i in rects:
		plt.text(i.get_x()+i.get_width()/2,i.get_height()*1.03,i.get_height(),ha='center',va='bottom',fontsize='large')


x=np.linspace(0,len(l),len(l))
v=[i[1] for i in l]
name_list=[i[0] for i in l ]
print(name_list)
plt.ylim(0,130)
plt.title('浦中高二级姓氏人数前20',fontsize='x-large')
al(plt.bar(x,v,color=['b','pink','lime','yellow','royalblue'],tick_label=name_list))


plt.show()
