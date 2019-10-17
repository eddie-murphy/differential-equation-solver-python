#comparing numerical and exact solutions of example higher order diffy eq via graphing

import numpy as np
import matplotlib.pyplot as plt
from math import *

import numSolveDQ.modules.dqsolve as dqs
import numSolveDQ.modules.function as fun

#diffy eq is: 
    # of order 3
    #init conds: y''(x=0)=0, y'(x=0)=-1 , y(x=0)=0
    #eq is: 1*y''' = -4*y'' -6*y' -4*y +1
new=dqs.DifferentialEquation(3,[0,-1,0],[1,-4,-6,-4],1)
ans=new.nsolve(.05,0,5)
ans.graph()
#exact solution:
x=[j for j in list(np.arange(0,5,.05))]
y=[1/4 + exp(-t)*(cos(t) - 5*sin(t)/2) - 5*exp(-2*t)/4 for t in list(np.arange(0,5,.05))]
sus=fun.InterpolatingFunction(x,y,0,5)
sus.graph()

#plotting both to compare 
plt.plot(ans.x,ans.y,'r--',x,y)
plt.show()
