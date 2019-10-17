#Neville's algorithm for finding a polynomial given a list of data so that I can find a point for solution.
#takes list of x, and list of y, and x value that is desired.

import numSolveDQ.modules.errors as er

#a list with a smaller step size means a better approximation of value...same idea with
def neville(x, y, x0):
    if len(x)==len(y):
        n = len(x)
        p = n*[0]
        for k in range(n):
            for j in range(n-k):
                if k == 0:
                    p[j] = y[j]
                else:
                    p[j] = ((x0-x[j+k])*p[j]+(x[j]-x0)*p[j+1])/(x[j]-x[j+k])
        return p[0]
    else:
        raise er.LengthError()
