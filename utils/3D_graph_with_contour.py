import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np



def plot3d_with_contour(x, y, funct, x_label = 'x', y_label = 'y', z_label = 'z', cmap='coolwarm'):

    '''
    Plots a 3d map with contour
    Input:  x : range of values for x-axis
            y : range of values for y-axis
            x_label : label values for x-axis
            y_label : label values for x-axis
            z_label : label values for x-axis
    Output: 3d figure of the surface along with the filled contourf
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    X, Y = np.meshgrid(x, y)
    Z = funct(X, Y)

    surf_obj = ax.plot_surface(X,Y,Z, cmap=cmap)
    fig.colorbar(surf_obj)
    # plt.show()

    z_min = np.min(Z)

    ax.contourf(X,Y,Z, offset=z_min, cmap=cmap)
    plt.show()



def funct(x, y):
    return x**3 + y**2

if __name__ == '__main__':
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)

    plot3d_with_contour(x, y, funct)

    print(funct(1,2))
