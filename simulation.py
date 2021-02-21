import numpy as np
import matplotlib.pyplot as plt


x_range = np.linspace(0, 5, 1000)
y_range = -x_range/2
z_range = np.sin(10*x_range)
"""
# Simple way
# Easy, not powerful
plt.plot(x_range, y_range)
plt.xlabel("Mack")
plt.show()
"""


# Hard way
# Powerful
fig, ax = plt.subplots(1)
ax.plot(x_range, y_range, label="1/2", color="cyan")
ax.plot(x_range, z_range, label="sin", color="pink")
ax.grid(alpha=0.2)
ax.set_xlabel("Mack")
ax.legend()