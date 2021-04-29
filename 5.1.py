import numpy as np
import matplotlib.pyplot as plt

A = np.array([[3, 7], [2, 6]])

plt.xlim(0,10)
plt.ylim(0,10)

plt.quiver([0,0],[0,0], A[:,0], A[:,1],angles='xy', scale_units='xy',scale=1,color=['Magenta','Crimson'])

plt.title("Lab 5.1")
plt.grid()
plt.show()
