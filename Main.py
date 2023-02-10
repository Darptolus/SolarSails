import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axes
fig, ax = plt.subplots(figsize=(9,9))

# Set up plot limits
# The astronomical unit [AU] (150,000,000 km)
# 1 Billion km = 1,000'000,000 km
# Perihelion - Aphelion
# Mercury   0.307-0.588 AU  or  45.9–88.0       million km  AVG 0.4475  AU
# Venus     0.718-0.728 AU  or  107.4–108.9     million km  AVG 0.723   AU
# Earth     0.983-1.017 AU  or  147.1–152.1     million km  AVG 1       AU
# Mars      1.382-1.666 AU  or  206.7–249.2     million km  AVG 1.524   AU
# Jupiter   4.951-5.457 AU  or  740.7–816.4     million km  AVG 5.204   AU
# Saturn    9.075-10.07 AU  or  1.3576–1.5065   billion km  AVG 9.5725  AU
# Uranus    18.27-20.06 AU  or  2.733–3.001     billion km  AVG 19.165  AU
# Neptune   29.89-30.47 AU  or  4.471–4.558     billion km  AVG 30.18   AU
# Pluto     29.7-49.5   AU  or  4.44-7.41       billion km  AVG 39.6    AU

limit = 12

ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)

# Set up plot titles and labels
plt.title("Solar Sail Simulation")
plt.xlabel("Distance (Billion Kilometers)")
plt.ylabel("Distance (Billion Kilometers)")

# Create circle patch for the planets orbits & sun
circ_Sun = plt.Circle((0, 0), 0.00465047, color='r', fill=True)
ax.add_patch(circ_Sun)

circ_Mercury = plt.Circle((0, 0), 0.4475, color='b', fill=False)
ax.add_patch(circ_Mercury)

circ_Venus = plt.Circle((0, 0), 0.723, color='b', fill=False)
ax.add_patch(circ_Venus)

circ_Earth = plt.Circle((0, 0), 1, color='b', fill=False)
ax.add_patch(circ_Earth)

circ_Mars = plt.Circle((0, 0), 1.524, color='b', fill=False)
ax.add_patch(circ_Mars)

circ_Jupiter = plt.Circle((0, 0), 5.204, color='b', fill=False)
ax.add_patch(circ_Jupiter)

circ_Saturn = plt.Circle((0, 0), 9.5725, color='b', fill=False)
ax.add_patch(circ_Saturn)

#circ_Uranus = plt.Circle((0, 0), 1, color='b', fill=False)
#ax.add_patch(circ_Uranus)

#circ_Neptune = plt.Circle((0, 0), 1, color='b', fill=False)
#ax.add_patch(circ_Neptune)

# circ_Pluto = plt.Circle((0, 0), 39.6, color='b', fill=False)
# ax.add_patch(circ_Pluto)

# Create circle patch for the smaller circle
circ_small = plt.Circle((0, 0), 0.1, color='r', fill=True)
ax.add_patch(circ_small)

spacing1 = 0.2
spacing2 = 0.6

plt.text(-limit + spacing1, -limit+spacing2*6, 'Speed:', fontsize=10)
plt.text(-limit + spacing1, -limit+spacing2*5, 'Acceleration:', fontsize=10)
plt.text(-limit + spacing1, -limit+spacing2*4, 'Position: (,)', fontsize=10)
plt.text(-limit + spacing1, -limit+spacing2*3, 'Force:', fontsize=10)
plt.text(-limit + spacing1, -limit+spacing2*2, 'Disance from earth:', fontsize=10)
plt.text(-limit + spacing1, -limit+spacing2, 'Disance from sun:', fontsize=10)

# Initialize variables for animation
theta = 0
dt = 0.1

# Define update function for animation
def update(num):
    global theta
    
    # Update the position of the smaller circle
    x, y = circ_small.center
    circ_small.center = (np.cos(theta), np.sin(theta))
    
    # Update angle
    theta += dt

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 2*np.pi, dt), repeat=True)
# plt.rcParams['figure.figsize'] = [10,10]
plt.show()
