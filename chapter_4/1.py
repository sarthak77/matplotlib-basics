import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot([1, 2, 3], [1, 2, 3]);
ax2 = fig.add_subplot(212)
ax2.plot([1, 2, 3], [3, 2, 1]);
plt.show()

"""
fig = plt.figure()
: This function returns a Figure where we can add one or more Axes
instances.

ax = fig.add_subplot(111)
: This function returns an Axes instance, where we can plot (as done
so far), and this is also the reason why we call the variable referring
to that instance ax (from Axes). This is a common way to add an Axes 
to a Figure, but add_subplot() does a bit more: it adds a subplot. So 
far we have only seen a Figure with one Axes instance, so only one area
where we can draw, but Matplotlib allows more than one.

add_subplot() takes three parameters:
fig.add_subplot(numrows, numcols, fignum)
where:
•
numrows
 represents the number of rows of subplots to prepare
•
numcols
 represents the number of columns of subplots to prepare
•
fignum
 varies from 
1 to numrows*numcols and specifies the current subplot (the one used now)
"""