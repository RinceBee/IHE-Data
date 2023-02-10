import matplotlib.pylab as plt
import scipy as sp
import numpy as np
import time

plt.ion()
tstart = time.time()
x = np.arange(0, 2*sp.pi, 0.01)
line, = plt.plot(x,np.sin(x))
for i in np.arange(1,200):
    line.set_ydata(sp.sin(x+i))
    plt.draw()

print 'FPS:', 200
