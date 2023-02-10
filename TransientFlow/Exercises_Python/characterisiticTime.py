from numpy import pi
#from scipy import pi
#import numpy as np

L=500000
kD = 500
S = 0.15
T = (L/pi)**2 * S/kD
print '\nT = %.2f days, or, equivalentluy, %.2f years' % (T,T/365.25)
