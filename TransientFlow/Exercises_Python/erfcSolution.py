import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from numpy.special import erfc
kD = 1200 # m2/d
Sy = 0.2  # -
A  = 1    # m

x = np.linspace(0,1000,1001)
t = np.linspace(0,  20, 200)
t = 1;

u = np.sqrt(( x**2 * Sy ) / (4 * kD * t))

s = A * np.erfc(u)

plt.figure(figsize=(8,5))
plt.plot(x,t)
