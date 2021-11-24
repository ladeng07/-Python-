import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
a=pd.read_csv('Updates_NC.csv')
print(a)
print(a.columns)
print(a[a['报道时间'].isin(['2月17日',])])
l1=a[a['报道时间'].isin(['2月17日',])]
l=list(set(a['省份']))
l2=[]

print(l)
print(len(l))
print(a['新增确诊'].sum())
p=a[a['报道时间'].isin(['2月17日'])]
ren=[p[p['省份'].isin([i])]['新增确诊'].sum() for i in l]
#print(dict((zip(l,ren))).values())
total=sorted(dict((zip(l,ren))).items(),key=lambda item:item[1] ,reverse=True)

#print(zip(*total))
z=list(zip(*total))
z=[i for i in z[1] if i!=0]
print(z[1])
x=np.linspace(1,len(z),len(z[1:]))
print(x)
plt.bar(x,z[1:],label='graph 1')
plt.show()
