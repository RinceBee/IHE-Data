import numpy as np
import matplotlib.pylab as plt

L  = 200. # width of system in m
kD = 200. # transmissivity of aquifer m2/d
Sy = 0.2   # specific yield, [-]
A  = 1.0  # iniital head increase [m]
x = np.linspace(-L/2.,L/2,100)
F  = 4 * A / np.pi

t  = 0.5  # time in d

T = (L/np.pi)**2 * Sy/kD

s = np.zeros_like(x)
for j in range(1,21):
    s = s + F * (-1)**(j-1) / (2*j-1) * np.cos((2*j-1)*np.pi*x/L) * np.exp(-(2*j-1)**2*t/T)

plt.figure
plt.plot(x,s)
