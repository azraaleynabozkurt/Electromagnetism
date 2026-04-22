import numpy as np
import matplotlib.pyplot as plt

q = 1.0    
m = 1.0     
B_z = 2.0   
v_perp = 5.0 -
v_z = 1.0    

omega = (q * B_z) / m  

radius = (m * v_perp) / (q * B_z)

t = np.linspace(0, 5 * (2 * np.pi / omega), 1000)

x = radius * np.cos(omega * t)
y = radius * np.sin(omega * t)
z = v_z * t

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z, label='Trajectory of a Charged Particle', color='purple', linewidth=2)

for i in range(0, 10, 2):
    ax.quiver(0, 0, i, 0, 0, 2, color='red', alpha=0.5, arrow_length_ratio=0.1)

ax.set_title('Lorentz Force: Helical Path of a Charged Particle in a Uniform B-Field')
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
ax.set_zlabel('Z Position')

ax.text2D(0.05, 0.95, "Red Arrows: Uniform Magnetic Field ($B$)\nPurple Line: Particle Trajectory", 
          transform=ax.transAxes, fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

plt.savefig('lorentzforce.png', dpi=300, bbox_inches='tight')
ax.legend()
plt.show()