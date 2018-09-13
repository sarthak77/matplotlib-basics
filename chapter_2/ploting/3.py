import matplotlib.pyplot as plt
x = range(1, 5)
plt.plot(x, [xi*1.5 for xi in x])
plt.plot(x, [xi*3.0 for xi in x])
plt.plot(x, [xi/3.0 for xi in x])
#floating values to avoid typecasting
plt.show()

"""
The multiline plot is possible because, by default, the 
hold
 property is enabled 
(consider it as a declaration to preserve all the plotted lines on the current figure 
instead of replacing them at every 
plot()
 call).
"""