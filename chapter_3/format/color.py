import matplotlib.pyplot as plt 
import numpy as np 
y = np.arange(1, 3) 
plt.plot(y, 'y');#semi colon to supress the output of functions
plt.plot(y+1, 'm');
plt.plot(y+2, 'c');
plt.show()

"""
Here is a table of the abbreviations used to select colors:
| Color abbreviation |  Color Name
| b                  |  blue
| c                  |  cyan
| g                  |  green
| k                  |  black
| m                  |  magenta
| r                  |  red
| w                  |  white
| y                  |  yellow

"""
#other way
"""
In [1]: import matplotlib.pyplot as plt 
In [2]: import numpy as np 
In [3]: y = np.arange(1, 3) 
In [4]: plt.plot(y, 'y', y+1, 'm', y+2, 'c');
In [5]: plt.show()
"""