import numpy as np
import matplotlib.pyplot as plt
#n=12
#x=np.arange(n)
#print(x)
#n = 12
#X = np.arange(n)
#print(X)
#Y1 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)
#Y2 = np.random.uniform(0.5, 1.0, n)
#print(Y1)
#print(Y2)
n=1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
plt.scatter(X,Y)
plt.xticks(())
plt.yticks(())
plt.show()
