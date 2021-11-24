import pandas as pd
import collections
import numpy as np
import matplotlib.pyplot as plt

ex=pd.read_excel('2019年12月学业水平考试2018级考生成绩.xls')
print(ex.iloc[1:,5])
'''wl=[i for i in ex.iloc[1:,5]]
hx=[i for i in ex.iloc[1:,6]]
sw=[i for i in ex.iloc[1:,7]]
c=collections.Counter(wl)
print(c.most_common())

v=[i[1] for i in sorted(collections.Counter([i for i in ex.iloc[1:,5+i]]).most_common())]
name_list=[i[0] for i in sorted(c.most_common())]

al(plt.bar(x,v,color='r',tick_label=name_list))
plt.show()
'''
def al(rects):
	n=0
	for i in rects:
		plt.text((i.get_x()+i.get_width())/2,i.get_height(),i.get_height(),ha='right',va='bottom')
for e in range(0,5):
	c=sorted(collections.Counter([i for i in ex.iloc[1:,5+e]]).most_common())
	x=np.linspace(0,len(c),len(c))
	v=[i[1] for i in c]
	name_list=[i[0] for i in c]
	plt.subplot(231+e)
	al(plt.bar(x,v,color='r',tick_label=name_list))
plt.show()