import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
a=pd.read_csv('DXYOverall.csv')
print(a.columns)
print(a.shape)


def get_l(df):
	day=24
	mon=1
	date=[]
	l2=[]
	for i in range(a.shape[0]-1,0,-1):
		if day < 32 and day != int(df.loc[i,'updateTime'][8:10]) :
			l2.append(i+1)
			date.append(str(mon)+'/'+str(day))
			day +=1
		elif day >31:
			day=1
			mon+=1
	l2.append(0)
	date.append(str(mon)+'/'+str(day))
	return l2,date
	
	  
def main(num):
	if num <6:
		yv=80000
	else:
		yv=18000
	cc=list(a.loc[l2,lt[num]])
	x=np.linspace(0,len(cc),len(cc))
	plt.figure(figsize=(12,4))
	ax = plt.gca()
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	plt.scatter(x, cc, s = 10, color = 'black')
	plt.plot(x,cc,color='red',linewidth=2)
	plt.ylim(0,yv)
	plt.grid(axis="y",linestyle='-.')
	plt.title('DXY Charts')
	plt.xlabel('Time')
	plt.ylabel('Counts')
	plt.xticks(x,date)
	#plt.savefig('hhh.png')
	plt.show()
	
	
l2,date=get_l(a)
lt=['currentConfirmedCount', 'confirmedCount',
       'suspectedCount', 'curedCount',
       'deadCount', 'seriousCount',
       'suspectedIncr', 'currentConfirmedIncr',
       'confirmedIncr', 'curedIncr',
       'deadIncr', 'seriousIncr',]
       
main(1)