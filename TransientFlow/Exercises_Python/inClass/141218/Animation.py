# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #The propagation of a wave of the state in the surface water level on the head in adjacent groundwater.
#
# The solution is
#
# $$ s = s_0 e^{-ax} sin \left( \omega t - a x \right) $$

print 'starting'

import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation

print 'setting parameters'

kD   = 1200  # m2/d
S    = 0.002 # specific yield
s0   = 1.0   # wave amplitude
omega = 4*np.pi # tide twice a day
a = np.sqrt(S * omega/(2 * kD))

print 'defining x and time'

x = np.linspace(0,1000,500)
time = np.arange(0,1,0.05)

print 'defining dd(x,t)'

def dd(x,t):
  return s0 * np.exp(-a*x)*np.sin(omega*t-a*x)

print 'plotting graphs'

for t in time:
  plt.plot(x,dd(x,t))

plt.hold('on')

print 'plotting envelopes'

plt.plot(x, s0*np.exp(-a*x), linewidth=5); # envelope
plt.plot(x,-s0*np.exp(-a*x), linewidth=5); # envelope

plt.xlim(0,1000)

print 'plot empbellishments'

plt.xlabel('x [m]'); plt.ylabel('head change s [m]');
plt.title('head as fuction of x from river at different times');

print 'First part done'

print 'Animation starts'

fig = plt.figure()
ax = plt.axes(xlim=(0, 1000), ylim=(-s0, s0))
line, = ax.plot([], [], lw=2)

print 'defining init()'

def init():
  line.set_data([], [])
  return line

print 'defining animate()'

def animate(it,args): # Plot a moving sine wave x = np.linspace(0, 2, 1000)
    x,time,line = args
    print it
    print x[1:3]
    print line
    y = dd(x,time[it])
    line.set_data(x, y)
    print it
    return line

print 'running ainmation'

anim = animation.FuncAnimation(fig, animate, [x, time, line],
        init_func=init, interval=10)

print 'show plots'

plt.show()

# <codecell>
