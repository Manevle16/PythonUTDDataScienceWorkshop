import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 100)
y = x*2
z = x * 2 * 2
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')
plt.show()
