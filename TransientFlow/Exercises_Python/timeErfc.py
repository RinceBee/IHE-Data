# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pylab as plt
from scipy import special

#%%
kD = 1200 # m2/d
Sy = 0.2  # -
A  = 1.0  # m
L  = 500  # m

#%% times and distances to be used
times = np.linspace(0,200,201)  # d
X     = np.linspace(0,L,101)

# edit first time to not let it be zero
times[0] = times[1]/100


#%% prepare axes of both plots
fig,(ax1,ax2) = plt.subplots(2,1, sharey=True)

ax1.set_title('Effect of a sudden change of head at x=0')
ax2.set_title('Effect of a sudden change of head at x=0')
ax1.set_xlabel(' x [m]')
ax2.set_xlabel(' time [d]')
ax1.set_ylabel(' elevatin [m]')
ax2.set_ylabel(' elevatin [m]')
ax1.set_xlim(X[0],X[-1])
ax2.set_xlim(times[0],times[-1])
ax1.set_ylim(0, A)
ax2.set_ylim(0, A)

ax1.grid(True)
ax2.grid(True)

#%% compute for various times and all distances
for t in times[::20]:
    u = X * np.sqrt(Sy / (4 * kD * t))
    s = A * special.erfc(u)
    ax1.plot(X,s, label='t=%.2f' % t)

ax1.legend()

#%% compute for verious distrance and all times
for x in X[::20]:
    u = x * np.sqrt(Sy / (4 * kD * times))
    s = A * special.erfc(u)
    ax2.plot(times,s, label='x=%.2f' % x)

ax2.legend()




