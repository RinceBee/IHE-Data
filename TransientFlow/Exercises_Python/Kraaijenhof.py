import numpy as np
from   numpy import pi
import matplotlib.pyplot as plt
#pylab

def kraaijenhof(A,L,x,T,t):
    p = -4*A/pi;
    dd = np.zeros_like(x)
    for j in range(1,21):
        p =-p;
        s = p * (1/(2*j-1) *
                 np.cos( (2*j-1)*pi*x/L) *
                 np.exp(-((2*j-1))**2 * t/T)
                 )
        print s[::20]
        dd += s
    return dd

## parameters
kD     = 900 # m2/d
S      = 0.2 # -
A      = 1.0 # m
L      = 200 # m
x      = np.linspace(-L,L,100)/2

T      = (L/pi)**2 * S/kD
Dt50   = np.log(2)* T
times  = np.hstack((np.arange(1,20) * Dt50/20, np.arange(1,20) *  Dt50))

#plt.close()

plt.axes(xlabel='time [h]', ylabel='stage [m]', ylim=(0, 1.5*A))
plt.title('head decay of groundwater system between parallel head boundaries')
plt.hold(True)


h=[]
for t in times[:3]:
    #import pdb; pdb.set_trace()
    dd = kraaijenhof(A,L,x,T,t)
    plt.plot(x,dd)
    print dd[::20]
    print
#    plt.show()
    plt.pause(0.02)
