import numpy as np
import inspect

def Wh0(u,Rho,limit=20,N=2000):
    '''
    Hantush's well function  w = W(u,r/lambda,limit=20,N=2000)
    limit is upper integration boundary 10**limit
    N is number of points on which the argument is integrated.

    s = Wh(u,rho,limit=20,N=2000)

    First version, works for one u and one rho
    '''
    assert np.size(u)  ==1, "This version of Wh(u,rho) only works for one u at a time"
    assert np.size(Rho)==1, "This version of Wh(u,rho) only works for one rho at a time"

    # integration variable should span from min(u) to infinity
    # limit and N should be large ennough, for accuracy
    y   = np.logspace(np.log10(u), limit, N)
    dy  = np.diff(y)

    f   = np.exp(-y -  Rho**2 / 4.0 / y) / y
    fdy = (f[:-1] + f[1:]) * dy/2
    return np.sum(fdy)


def test_Wh0(u,Rho):
    myName = inspect.stack()[0][3]
    print '\nTest %s' % myName
    print __name__
    print '%10s' % 'u --> ',
    for u in U:
        print ' %10.4g' % u,
    print
    print '%-10s%10s' % ('Rho','W-->')
    for rho in Rho:
        print '%10.4g' % rho,
        for u in U:
            print ' %10.4g' % Wh0(u,rho),
        print


# =======Second version works for any number of u but only one rho =====
def Wh(u,Rho,limit=20,N=2000):
    '''
    Hantush's well function  w = W(u,r/lambda,limit=20,N=2000)
    limit is upper integration boundary 10**limit
    N is number of points on which the argument is integrated.

    s = Wh(u,rho,limit=20,N=2000)

    u can have any shape, but must be a np.array, Rho musbt a scalar

    W(u,Rho) will have the same shape as u
    '''

    if type(u)==float: u = [u]

    u      = np.asarray(u)
    uShape = u.shape  # chapture the shape of u
    u      = u.ravel()

    assert np.size(Rho)==1, "Rho must be a scalar"

    # integration variable should span from min(u) to infinity
    y   = np.logspace(np.log10(min(u)), limit, N)
    dy  = np.diff(y)

    f   = np.exp(-y -  Rho**2 / 4.0 / y) / y
    fdy = np.hstack( ( (f[:-1] + f[1:]) * dy/2, 0 ) )

    # integrate from any u to infinity by cumsum from the back
    # for this we need to reverse the fdy array twice
    Fdy = np.cumsum(fdy[-1::-1])[-1::-1]

    # to get the values at the real u justinterpolate
    Wh   = np.interp(u, y, Fdy, left=Fdy[0])

    return Wh.reshape(uShape)

def test_Wh(U,Rho):
    myName = inspect.stack()[0][3]
    print '\nRunning test %s' % myName
    print
    print 'U-values'
    print U
    print
    print 'Corresponding Wh values'
    print Wh(U,Rho)


if __name__ == '__main__':

    # test Wh0
    U = [0.0001, 0.001, 0.01, 0.1, 1]
    Rho = [0.2, 0.5, 1]
    test_Wh0(U,Rho)

    # test Wh
    # test the function
    Rho = 0.01
    U1 = 0.001;
    U2 = [0.0001, 0.001, 0.01, 0.1];
    U3 = np.array([0.00001, 0.0001, 0.001, 0.01, 0.1, 1]);
    test_Wh(U1,Rho)
    test_Wh(U2,Rho)
    test_Wh(U3,Rho)
    test_Wh(U3.reshape((2,3)),Rho)
