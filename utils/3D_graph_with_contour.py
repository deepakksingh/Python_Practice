import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.random.randn(1,1000)
y = np.random.randn(1,1000)
z = x**2 + y**2 + 2*x + 2*y

# x_val, y_val = np.meshgrid(x,y)
# z_val = x_val**2+ y_val**2
# plt.contour(x_val, y_val,z_val)
# plt.show()

ax.plot_surface(x, y, z)
plt.show()

# plt.contourf(x_val, y_val, z_val)
# plt.show()