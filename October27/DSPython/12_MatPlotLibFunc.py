# Plotting Library for Python
# Similar feel to MatLab's graphical Plotting
# Conda Install matplotlib
# Visit matplotlib.org
# important link is gallery
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 11) #Returns 11 evenly spaced numbers from 0 to 5
y = x ** 2
print(x)
print(y)
# FUNCTIONAL method
plt.plot(x, y) #plots x values on x and y values on y axis
#plt.show()

plt.xlabel('X Label') #Gives x axis a label
plt.ylabel('Y Label') #Gives y axis a label
plt.title('Title') #Gives a title to the graph
#plt.show()

# Mutliplot
plt.subplot(1, 2, 1)  #Designates number of rows and columns and plots graph in position 1
plt.plot(x, y, 'r')
#plt.show()

plt.subplot(1, 2, 2) #Plots in position 2, if different # of rows and cols, will overwrite previous
plt.plot(y, x, 'b')
plt.show()
