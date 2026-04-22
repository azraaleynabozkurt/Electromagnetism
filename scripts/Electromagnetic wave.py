import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(0, 4 * np.pi, 100)

E = np.sin(x)
B = np.sin(x)

zeros = np.zeros_like(x)

ax.plot(x, E, zeros, label='Electric Field (E)', color='blue', linewidth=2)
ax.plot(x, zeros, B, label='Magnetic Field (B)', color='red', linewidth=2)

for i in range(0, len(x), 3):
    ax.plot([x[i], x[i]], [0, E[i]], [0, 0], color='blue', alpha=0.4)
    ax.plot([x[i], x[i]], [0, 0], [0, B[i]], color='red', alpha=0.4)

ax.set_title('Electromagnetic Wave')
ax.set_xlabel('Direction of Propagation (x)')
ax.set_ylabel('Electric Field')
ax.set_zlabel('Magnetic Field')

plt.savefig('electromagneticwave.png', dpi=300, bbox_inches='tight')
ax.legend()
plt.show()