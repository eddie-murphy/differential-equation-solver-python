#program that walks user through using my code to solve diffy qs

import numSolveDQ.modules.dqsolve as dqs

order=int(input("\n\nEnter the order of the differential equation. For example, if first order, enter 1; if 3rd order, enter 3.:\n"))
initial=[float(x) for x in input("\n\nEnter the initial conditions (at x=0) (one can change variables to turn a boundary into an intial condition) of the differential equation. Conditions are entered from left to right as y^n-1 to y, where n is the order of the diffy q. \nSeparate values with a comma: \n\n").split(",")]
if len(initial)==1:
    initial=initial[0]
else:
    pass
coeffs=[float(x) for x in input("\n\nEnter coeffs on y terms from left to right as y^n to y, do not include coeff on f(x). Coeffs need to be entered from the form y^n=y^n-1+y^n-2...+y. y^n can have a non-zero coeff.\nSeparate values with a comma: \n\n").split(",")]
isthereyp=input("\n\nIs there an f(x)? That is to say, is there an f(x) that appears like it does in these equations: y''+y'+y=f(x) or y'=y+f(x) or y'=y*f(x). If so enter yes, else enter no:\n\n")
if isthereyp=="yes":
    ypfunction=input("\n\nEnter f(x). If f(x)=3cos(5x) then enter 3*cos(5*x). if f(x)=-3, enter -3:\n\n")
    if order==1:
        more=input("\n\nIs the differential equation nonlinear? (For instance, is y multiplied by f(x)?) Enter yes or no:\n\n")
        if more=='yes':
            ypoperator=input("\n\nUnder the assumption that this is nonlinear: How are y and f(x) related? Is it multiplication, division? If multiplication: enter * :\n\n")
        else:
            ypoperator="+"
    elif order>1:
        ypoperator="+"
else:
    ypfunction=''
    ypoperator="+"

print("\n\nWe are almost done!\n\n")
bounds=[float(x) for x in input("\n\nEnter the lower and upper values of the range of x's you want the equation solved for:\n\nSeparate values with a comma. Enter lower value, upper value: \n\n").split(",")]
lower=bounds[0]
upper=bounds[1]
h=.025

if order==1:
    dqans=dqs.FirstDEQ(initial,coeffs,ypfunction,ypoperator)
    ans=dqans.nsolve(h,lower,upper)
else:
    dqans=dqs.DifferentialEquation(order,initial,coeffs,ypfunction,ypoperator)
    ans=dqans.nsolve(h,lower,upper)
isgraph=input("\n\nDo you want the function graphed over the range of x you specified, enter yes or no. If yes, a graph window will open. Close the graph window once you are ready to continue:\n\n")
if isgraph=="yes":
    ans.graph()
else:
    pass
try:
    xvalues=[float(x) for x in input("\n\nEnter the values of x (within the earlier specified range) you want the numeric solution solved at:\n\nSeparate values with a comma. Don't enter anything if you don't want any values: \n\n").split(",")]
    for x in xvalues:
        print("\n\nThe function at",x,"=",ans.apply(x))
except ValueError:
    raise SystemExit

