import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0., np.e, 0.01)
y1 = np.exp(-x)
y2 = np.log(x)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(x, y1);
ax1.set_ylabel('Y values for exp(-x)');
ax2 = ax1.twinx()   # this is the important function
ax2.plot(x, y2, 'r');
ax2.set_xlim([0, np.e]);
ax2.set_ylabel('Y values for ln(x)');
ax2.set_xlabel('Same X for both exp(-x) and ln(x)');
plt.show()
"""
>>
The twinx() function does the trick: it creates a second set of axes,
putting the new ax2 axes at the exact same position of ax1, ready to be
used for plotting.
>>
This is the reason why we had to set the red color for the second line: the plot 
information was reset so that line would have been blue, as if it was
part of a completely new figure.
>>
The complementary function, twiny(), allows us to share the Y-axis with
two different X-axes.
"""