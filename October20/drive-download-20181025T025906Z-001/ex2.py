import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 100)
y = x*2
z = x * 2 * 2
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([.2, .5, .4, .4])
ax1.plot(x, y, color='red')
ax2.plot(x, y)
plt.show()
