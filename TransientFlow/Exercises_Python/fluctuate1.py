import numpy as np
import matplotlib.pyplot as plt
#pylab

def screenPos(f):
    '''reset window on screen to size given by fraction f
      where f may by a scalar or a tuple, and where all values
      are 0<=f<=1
    '''
    if type(f)==float: f=(f,) # assert we have a tuple
    mgr = plt.get_current_fig_manager()
    mgr.full_screen_toggle() # primitive but works
    py = mgr.canvas.height()
    px = mgr.canvas.width()
    mgr.resize(f[0]*px,f[-1]*py)
    return f[0]*px,f[-1]*py

#px,py = screenPos(0.8)


def fluctuate(kD,S,A,omega,t0,x,t):
    a = np.sqrt(omega * S / 2 / kD)
    s = A * np.exp(-a*x)
    if not t:
        return s
    else:
        return s * np.sin(omega * (t-t0) - a * x)

kD = 900 # m2/d
S  = 0.2 # -
A  = 1.0 # m
omega = 2*np.pi / 12  # rad/h
t0 = 1.0 # h
x  = np.linspace(0,1500,1500)
times = np.linspace(0,48,4*48)

plt.close()

plt.axes(xlabel='time [h]', ylabel='stage [m]', ylim=(-A,A))
screenPos(0.75)

s = fluctuate(kD,S,A,omega,[],x,[])
plt.plot(x,s,'r',x,-s,'r')

h=[]
for i,t in enumerate(times):
    if i==0:
        h = plt.plot(x, fluctuate(kD,S,A,omega,t0,x,t))
        h=h[0]
        #plt.hold(True)
    else:
        h.set_ydata(fluctuate(kD,S,A,omega,t0,x,t))
        plt.show()
        plt.pause(0.002)
