#comparing numerical and exact solutions of example nonlinear first order diffy eq via graphing

from math import *
import numpy as np
import matplotlib.pyplot as plt

import numSolveDQ.modules.dqsolve as dqs
import numSolveDQ.modules.function as fun


son=dqs.FirstDEQ(1,[1,1],'1-2*x','*') # Solving the non linear diffy eq: y'=y*(1-2*x)
ans=son.nsolve(.025,0,2)
ans.graph()
#exact soln:
x=[j for j in list(np.arange(0,2,.025))]
y=[exp(t-(t*t)) for t in list(np.arange(0,2,.025))]
sus=fun.InterpolatingFunction(x,y,0,2)
sus.graph()
#plot to compare
plt.plot(ans.x,ans.y,'r--',x,y)
plt.show()

