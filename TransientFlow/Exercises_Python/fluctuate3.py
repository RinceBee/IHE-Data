import numpy as np
import matplotlib.pyplot as plt
#pylab

def fluctuate(kD,S,A,omega,t0,x,t):
    a = np.sqrt(omega * S / 2 / kD)
    return A * np.exp(-a*x) * np.sin(omega*(t-t0) - a*x)

## parameters
kD     = 900 # m2/d
S      = 0.002 # -
A_     = 1.0 # m
omega_ = 2*np.pi / 12  # rad/h
t0_    = 1.0 # h
x      = np.linspace(0,1500,1500)
times  = np.linspace(0,48,4*48)

## superposition of a number of waves
N = 10;
A     = A_     * np.random.rand(N)
omega = omega_ * 1/np.random.rand(N)
t0    = 24     * np.random.rand(N)

plt.close()

plt.axes(xlabel='time [h]', ylabel='stage [m]', ylim=(-sum(A),sum(A)))

h=[]
for i,t in enumerate(times):
    s = np.zeros_like(x)
    for j in range(N):
        s += fluctuate(kD,S,A[j],omega[j],t0[j],x,t)
    print s
    if i==0:
        h = plt.plot(x,s)
        h=h[0]
        #plt.hold(True)
    else:
        h.set_ydata(s)
        plt.show()
        plt.pause(0.05)
