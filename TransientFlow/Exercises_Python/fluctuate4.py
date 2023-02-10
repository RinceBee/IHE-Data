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
X      = [0, 10, 100, 500]
times  = np.linspace(0,48,4*48)

## superposition of a number of waves
N     = 7;
A     = A_     * np.random.rand(N)
omega = omega_ * 1/np.random.rand(N)
t0    = 24     * np.random.rand(N)

#A     = np.ones((N,1))/3.; A[0] = 1; A=np.cumprod(A)
#omega = 2*np.pi/24/A
#t0    = np.zeros_like(t0)

plt.close()

plt.axes(xlabel='time [h]', ylabel='stage [m]', ylim=(-sum(A),sum(A)))

h=[]
for x in X:
    s = np.zeros_like(times)
    for j in range(N):
        ss = fluctuate(kD,S,A[j],omega[j],t0[j],x,times)
        #plt.plot(times,ss,'r')
        s += ss
    plt.plot(times,s,'b')
    plt.show()
