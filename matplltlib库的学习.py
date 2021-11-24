import numpy as np
import matplotlib.pyplot as plt#约定俗成的写法plt
x=np.linspace(-10,10,1000)#X轴数据
y=(16-x**2)**(1/2)
y2=-(16-x**2)**(1/2)
y3=np.sin(x)
y4=np.cos(x)
plt.xlim((-2*np.pi,2*np.pi))  # x参数范围
plt.ylim((-4,4))  # y参数范围
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 定义x轴和y轴的位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
l1,=plt.plot(x,y,label='aaa')
l2,=plt.plot(x,y2,label='bbb')
l3,=plt.plot(x,y3,label='ccc')
l4,=plt.plot(x,y4,label='ddd')
plt.legend(handles=[l1, l2, l3,l4], 
           labels = ['aaa', 'bbb','ccc','ddd'], 
           loc = 'best'
          )
plt.plot(x,y)
plt.show()