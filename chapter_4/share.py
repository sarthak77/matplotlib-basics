import matplotlib as mpl
mpl.rcParams['font.size'] = 11.
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(11)
fig = plt.figure()
ax1 = fig.add_subplot(311)
ax1.plot(x, x);

ax2 = fig.add_subplot(312, sharex=ax1)
ax2.plot(2*x, 2*x);

ax3 = fig.add_subplot(313, sharex=ax1)
ax3.plot(3*x, 3*x);

plt.show()
"""
You'll observe that when zooming, panning, or performing other similar
activities on a subplot, all the others will be modified too, according
to the same transformation.
"""