# Plotting Library for Python
# Similar feel to MatLab's graphical Plotting
# Conda Install matplotlib
# Visit matplotlib.org
# important link is gallery
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 11)
y = x ** 2

# Object Oriented method
#fig = plt.figure()  # empty canvas
#axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # left, bottom, width, height percentage wise
#axes.plot(x, y)
#axes.set_xlabel('X Label')
#axes.set_ylabel('Y Label')
#axes.set_title('Set Title')
#plt.show()

fig = plt.figure() #Creates new canvas
#Can plot one graph on top of another
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])


axes2 = fig.add_axes([0.2, 0.15, 0.4, 0.3])
#plt.show()

axes2 = fig.add_axes([0.5, 0.15, 0.4, 0.3]) #returns graph which can have data plotted on it
#plt.show()

axes1.plot(x,y)
axes2.plot(y,x)
plt.show()
