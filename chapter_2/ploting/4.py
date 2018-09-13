import matplotlib.pyplot as plt 
x = range(1, 5) 
plt.plot(x, [xi*1.5 for xi in x], x, [xi*3.0 for xi in x], x, [xi/3.0 for xi in x]) 
plt.show()