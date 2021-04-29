import numpy as np
import matplotlib.pyplot as plt

A = np.array([[5, 7, 0], [3, 8, 0], [0, 4, 5]])

fig = plt.figure()
A1 = fig.gca(projection='3d')

A1.set_xlim([0, 10])
A1.set_ylim([0, 10])
A1.set_zlim([0, 10])
origin = (0, 0, 0)

A1.quiver(origin, origin, origin, A[:, 0], A[:, 1], A[:, 2],
         arrow_length_ratio=0.07, colors=['Yellow', 'Magenta', 'Crimson'])

plt.title("Lab 5.2")
plt.grid()
plt.show()
