import matplotlib.pyplot as plt 
import numpy as np 
y = np.random.randn(1000) 
plt.hist(y,20);
plt.show()

"""
Histogram plots group up values into bins of values. By default, 
hist()
 uses a 
bin
value of 10 (so only ten categories, or bars, are computed), but we can customize 
it, either by passing an additional parameter, for example, in 
hist(y, <bins>)
, or 
using the 
bin
 keyword argument as 
hist(y, bin=<bins>)
.
"""