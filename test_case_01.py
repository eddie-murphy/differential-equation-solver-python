#comparing numerical and exact solutions of example first order diffy eq via graphing and evaluating at x values
#testing homogenous

import matplotlib.pyplot as plt
import numpy as np
import numexpr as ne
from math import *

import numSolveDQ.modules.neville as nev
import numSolveDQ.modules.dqsolve as dqs
import numSolveDQ.modules.function as fun


bob=dqs.FirstDEQ(3,[1,-2]) # the dq being solved is: y'=-2y where 
ans=bob.nsolve(.025,0,10) #being solved from x=0 to x=10 in 0.025 increments
#smaller increments means better accuracy at the cost of execution time and storage
ans.graph()
#the exact soln:
x=[j for j in list(np.arange(0,10,.025))]
y=[3*exp(-2*i) for i in list(np.arange(0,10,.025))]
sus=fun.InterpolatingFunction(x,y,0,10)
sus.graph()
#plotting them together
plt.plot(ans.x,ans.y,'r--',x,y)
plt.show()
#show them zoomed in

#testing the computed soln to the known exact soln
#these should match:
print(ans.apply(3.73))
print(3*exp(-2*3.73))
#and these should match:
print(ans.apply(6.725))
print(3*exp(-2*6.725))

#plotting the error between the numerical and exact soln
error=fun.InterpolatingFunction(x,[ans.y[i]-sus.y[i] for i in range(0,len(ans.y)-1)],0,10)
plt.plot(error.x,error.y)
plt.ylabel('error')
plt.xlabel('x')
plt.show()

