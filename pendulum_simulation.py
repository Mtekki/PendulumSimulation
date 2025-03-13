import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
g = 9.81  # gravity (m/s^2)
L = 1.0   # length of the pendulum (m)
theta0 = np.pi / 4  # initial angle (45 degrees)
omega0 = 0.0        # initial angular velocity (rad/s)
t_max = 10.0        # total simulation time (s)
dt = 0.01           # time step (s)

# Time array
t = np.arange(0, t_max, dt)

# Arrays to store theta and omega values
theta = np.zeros_like(t)
omega = np.zeros_like(t)

# Initial conditions
theta[0] = theta0
omega[0] = omega0

# Numerical integration (Euler method)
for i in range(1, len(t)):
    # Update angular velocity
    omega[i] = omega[i-1] - (g / L) * np.sin(theta[i-1]) * dt
    # Update angle
    theta[i] = theta[i-1] + omega[i-1] * dt

# Convert polar coordinates to Cartesian coordinates
x = L * np.sin(theta)
y = -L * np.cos(theta)

# Animation setup
fig, ax = plt.subplots()
ax.set_xlim(-L*1.5, L*1.5)
ax.set_ylim(-L*1.5, L*1.5)
line, = ax.plot([], [], 'o-', lw=2)

# Animation function
def animate(i):
    line.set_data([0, x[i]], [0, y[i]])
    return line,

# Create animation
ani = FuncAnimation(fig, animate, frames=len(t), interval=dt*1000, blit=True)

# Show the animation
plt.title("Simple Pendulum Simulation")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

# Save the final frame as a PNG
plt.figure()
plt.plot([0, x[-1]], [0, y[-1]], 'o-', lw=2)
plt.xlim(-L*1.5, L*1.5)
plt.ylim(-L*1.5, L*1.5)
plt.title("Pendulum Simulation")
plt.savefig("pendulum.png")  # Save the plot as a PNG file
plt.show()