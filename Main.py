import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'ro')
fig, ax = plt.subplots()

def create_circle():
    circle = plt.Circle((0, 0), radius = 30, fill = False)
    return circle
def create_smallcircle():
    smallcircle = plt.Circle((30, 0), radius = 5, fill = False)
    return smallcircle
def update(frame):
    xdata.append(frame)

    ln.set_data(xdata, ydata)
    return ln,
def show_shape(patch_c, patch_sc):
    ax = plt.gca()
    ax.add_patch(patch_c)
    ax.add_patch(patch_sc)
    plt.text(30, 27, 'speed:', fontsize = 10)
    plt.text(30, 22, 'acceleration:', fontsize=10)
    plt.text(30, 17, 'position: (,)', fontsize=10)
    plt.text(30, 12, 'disance from center:', fontsize=10)
    plt.text(30, 7, 'force:', fontsize=10)
    #plt.axis('scaled')
    plt.axis([-80, 80, -80, 80])
    plt.axis('equal')

    ani = FuncAnimation(fig, update, frames=np.linspace(0, 360, 180),
                        init_func=init, blit=True)
    plt.show()
if __name__ == '__main__':
    c = create_circle()
    sc = create_smallcircle()
    show_shape(c, sc)
