import matplotlib.pyplot as plt 
import numpy as np 
x = np.arange(0.0, 6.0, 0.01) 
plt.plot(x, [x**2 for x in x]) #x and y axis
plt.show()