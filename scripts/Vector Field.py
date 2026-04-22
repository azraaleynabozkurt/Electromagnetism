import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

q1, pos1 = 1, [-1, 0]  
q2, pos2 = -1, [1, 0]  

def e_field(q, r0, x, y):
    den = np.hypot(x - r0[0], y - r0[1])**3
    return q * (x - r0[0]) / den, q * (y - r0[1]) / den

Ex1, Ey1 = e_field(q1, pos1, X, Y)
Ex2, Ey2 = e_field(q2, pos2, X, Y)

Ex = Ex1 + Ex2
Ey = Ey1 + Ey2

E_magnitude = np.sqrt(Ex**2 + Ey**2)

plt.figure(figsize=(9, 6))

plt.streamplot(X, Y, Ex, Ey, color=E_magnitude, linewidth=1.5, cmap='inferno', density=1.5)

plt.plot(pos1[0], pos1[1], 'ro', markersize=15, label='Positive Charge (+)')
plt.plot(pos2[0], pos2[1], 'bo', markersize=15, label='Negative Charge (-)')

plt.title("Vector Field of an Electric Dipole")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.colorbar(label="Electric Field Strength (Magnitude)")
plt.legend(loc='lower right')
plt.grid(False)
plt.savefig('vectorfield.png', dpi=300, bbox_inches='tight')
plt.show()