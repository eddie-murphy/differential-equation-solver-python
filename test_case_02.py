#comparing numerical and exact solutions of example first order diffy eq via graphing

import numpy as np
import matplotlib.pyplot as plt
from math import *

import numSolveDQ.modules.dqsolve as dqs
import numSolveDQ.modules.function as fun


son=dqs.FirstDEQ(3,[2,-4],'2*cos(4*x)') #The diffy eq being solved is: 2y'==-4y+2*cos(4*x), where y(x=0)=3
ans=son.nsolve(.025,0,2) #solving in 0.25 step increments from x=0 to x=2 
ans.graph() #graphs the solution in this range

#now to compare to the exact solution
x=[j for j in list(np.arange(0,2,.025))] #populating x values we will plug into the exact soln eq
#the below is the exact solution
y=[0.1*cos(4*t)+0.2*sin(4*t)+2.9*exp(-2*t) for t in list(np.arange(0,2,.025))]
sus=fun.InterpolatingFunction(x,y,0,2)
sus.graph()
#plotting both together to show that they match
plt.plot(ans.x,ans.y,'r--',x,y)
plt.show()