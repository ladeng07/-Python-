import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_json('population_data.json')
cl=sorted(list(set(list(df['Country Name']))))
n=cl[11]
'''
11Australia
42.china
34.canada
232UK
232US
242World
239vietnam
'''
df=df[df['Country Name'].isin([n,])]
print(cl)
#df=df[df['Country Code'].isin(['WLD',])]
print(df)
date=list(df['Year'])
value=list(df['Value'])
#value=[i/10**8 for i in value]
x=np.linspace(0,len(date),len(date))

plt.figure()
#plt.ylim(0,80)
plt.plot(x,value,color='r',linewidth=2)
plt.scatter(x,value,s=66,color='black')
plt.xticks(x,date)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('%s population' % n)
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.grid(axis='y',linestyle='-.')
plt.show()