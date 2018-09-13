import matplotlib.pyplot as plt 
import numpy as np 
x = np.arange(1, 5) 
plt.plot(x, x*1.5, x, x*3.0, x, x/3.0) 
print(plt.axis())  # shows the current axis limits values
plt.axis([0, 5, -1, 13])  # set new axes limits
plt.show()
"""
The list of values, that's the whole set of four values of keyword arguments 
[xmin,
xmax,
ymin,
ymax]
, allows us to specify at the same time, the minimum and 
maximum limits respectively for the X-axis and the Y-axis. We can use the specific 
keyword arguments, for example:
plt.axis(xmin=NNN, ymax=NNN)
If we wish to set only some of these limits (in the previous line, we set only the 
minimum value for X-axis and the maximum value for Y-axis). 
"""