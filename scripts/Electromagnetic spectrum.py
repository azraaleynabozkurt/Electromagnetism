import numpy as np
import matplotlib.pyplot as plt

c = 3e8                 
h_eV = 4.135667696e-15  

log_wavelengths = np.linspace(4, -14, 500)
wavelengths = 10**log_wavelengths

frequencies = c / wavelengths
energies_eV = h_eV * frequencies

log_freqs = np.log10(frequencies)
log_energies = np.log10(energies_eV)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(log_wavelengths, log_freqs, log_energies,
                     c=log_freqs, cmap='turbo', s=25, alpha=0.9)

regions = [
    ("Radio", 2, 6.47, -7.89),
    ("Microwave", -2, 10.47, -3.89),
    ("Infrared", -5, 13.47, -0.89),
    ("Visible", -6.3, 14.77, 0.41),
    ("Ultraviolet", -8, 16.47, 2.11),
    ("X-Ray", -11, 19.47, 5.11),
    ("Gamma", -13, 21.47, 7.11)
]

for name, wl, freq, energy in regions:
    ax.text(wl, freq, energy, f"  {name}", color='black',
            fontsize=10, fontweight='bold', zorder=5)

ax.set_title("Electromagnetic Spectrum\n(Wavelength vs. Frequency vs. Energy)",
             fontsize=15, pad=20, fontweight='bold')

ax.set_xlabel("Log10(Wavelength) [m]", fontsize=12, fontweight='bold')
ax.set_ylabel("Log10(Frequency) [Hz]", fontsize=12, fontweight='bold')
ax.set_zlabel("Log10(Energy) [eV]", fontsize=12, fontweight='bold')

ax.invert_xaxis()

ax.view_init(elev=25, azim=135)

cbar = fig.colorbar(scatter, ax=ax, shrink=0.5, pad=0.1)
cbar.set_label('Log10(Frequency) Intensity')

plt.tight_layout()
plt.savefig('_em_spectrum_.png', dpi=300, bbox_inches='tight')
plt.show()