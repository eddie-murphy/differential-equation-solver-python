import numpy as np
import numexpr as ne
import matplotlib.pyplot as plt
from math import *

import numSolveDQ.modules.neville as nev
import numSolveDQ.modules.function as fun
import numSolveDQ.modules.errors as er


class DifferentialEquation:
    def __init__(self,order,initialconds,coeffs,ypfunction='',ypoperator='+'):
        
        #coeffs entered from left to right as y^n to y, do not include f(x)
        #n is the level of derivative like n=2 is second derivative
        #coeffs (like a,b,c,and d) entered from the form a*y^n=b*y^(n-1)+c*y^(n-2)...+d*y as [a,b,c,d]
        #if a level of derivative does not exist, put a 0 in its place in the coeff list 
        #it is always highest order differential(derivative) to lowest in the coeff list
        #any terms with no x are included in the ypfunction
        #enter f(x) in ypfunction
        #initial conditions (at t==0) entered from left to right as y^n-1 to y
        #it is always highest order differential(derivative) to lowest in the initial conditions list

        self.order=order
        self.ypoperator=fun.bioperatorFunction(ypoperator)
        if coeffs[0]!=1:
            ypfunction=str(1/coeffs[0])+'*('+str(ypfunction)+')'
            coeffs=[x*(1/coeffs[0]) for x in coeffs]
        self.cond = initialconds
        self.coeffs = coeffs
        ypfunction=str(ypfunction)
        #I am trusting that user only entered in functions that are functions of x, otherwise they entered constants
        if len(ypfunction)==0:
            ypfunction=fun.StringFunction('0*x')
        else:
            try:
                ypfunction=fun.StringFunction(ypfunction)
            except (er.FunctionVariableInputError,IndexError):
                ypfunction=fun.StringFunction(ypfunction+"+(0*x)")
        self.func=ypfunction

    def nsolve(self,h,lower,upper):
        #constant coefficients
        q0=np.matrix(str(self.cond)).transpose()
        t=list(np.arange(lower,upper+h,h))
        a=np.matrix(np.zeros((self.order,self.order)))
        a[:(self.order-1),1:]=np.identity(self.order-1)
        coeffs=self.coeffs
        coeffs=coeffs[::-1]
        coeffs=coeffs[:-1]
        a[-1:]=coeffs
        qstar=np.matrix(np.zeros((self.order,len(t))))
        qstar[:,0]=q0
        for i in range(0, len(t) - 1):
            b=np.matrix(np.array([[0],[0],[self.func.apply(i)]]))
            k1=a*qstar[:,i]+b
            q1=qstar[:,i]+k1*h/2
            k2=a*q1+b
            qstar[:,i+1]=qstar[:,i]+k2*h
        return fun.InterpolatingFunction(t, np.array(qstar)[0],lower,upper)

class FirstDEQ(DifferentialEquation):
    
    #this class if for first order dq eqs only
  

    def __init__(self,initialconds,coeffs,ypfunction='',ypoperator="+"):
        super().__init__(1,initialconds,coeffs,ypfunction,ypoperator)
        
        #enter coeffs left to right as if the equation is in form: y'=y+yp or y'=y*yp
        #this " y' " is called "y prime" and represents the first derivative of y
        #do not enter a coeff for yp if it is zero. 
        #by ypoperator I mean the operator (such as plus, minus,multiplication) between y and yp, entered like * or - or +, although plus is not necessary
        #a negative can go in for yp or in for the ypoperator, but you will accidentally cancel the negatives out if you put in both
        #better to only use the last argument when using not addition or subtraction of yp on y
        #coeffs: only those on terms with y in it, do not include coeffs of ypfunction. Include any coeffs of yp in yp arguement
        #for yp:
            #if postive, don't need to include + , or '*' if multiplying
            #if after arranging eq into the specified form and yp=-2*cos(2*x) then type -2*cos(2*x)

    def nsolve(self,h,lower,upper):
        #h is step, then lower and upper bounds the numeric solution is to be good for
        y0=self.cond
        t=list(np.arange(lower,upper+h,h))

        ystar=len(t)*[0]
        ystar[0]=y0
        ypfunction=self.func
        op=self.ypoperator
        for i in range(0, len(t) - 1):
            k1 = op.apply(self.coeffs[1] * ystar[i] , ypfunction.apply(t[i]))
            y1 = ystar[i] + k1 * h / 2
            k2 = op.apply(self.coeffs[1] * y1 , ypfunction.apply(t[i] + h / 2))
            y2 = ystar[i] + k2 * h / 2
            k3 = op.apply(self.coeffs[1] * y2 , ypfunction.apply(t[i] + h / 2))
            y3 = ystar[i] + k3 * h
            k4 = op.apply(self.coeffs[1] * y3 , ypfunction.apply(t[i] + h))
            ystar[i + 1] = ystar[i] + (k1 + 2 * k2 + 2 * k3 + k4) * h / 6
        return fun.InterpolatingFunction(t, ystar,lower,upper)






