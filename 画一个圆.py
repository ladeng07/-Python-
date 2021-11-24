import matplotlib.pyplot as plt
import numpy as np
h=np.linspace(0,2*np.pi,1000)
r=1
x=r*np.cos(h)
y=r*np.sin(h)
plt.figure(figsize=(8,8))
plt.plot(x,y)
plt.savefig('圆.png')
plt.show()