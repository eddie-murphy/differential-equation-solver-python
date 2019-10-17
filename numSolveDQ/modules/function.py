#from numSolveDQ.modules.neville import *
import numSolveDQ.modules.neville as nev
import matplotlib.pyplot as plt
import numexpr as ne
import operator

import numSolveDQ.modules.errors as er

class Function: #this is very much an abstract superclass for my program.
    def __init__(self,arg):
        self.func=arg

    def apply(self,x):
        return self.func(x)


def getop(op):
    return {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '^': operator.xor,
    }[op]
#takes string form of operator, and uses two things on sides of operator
class bioperatorFunction(Function):
    def __init__(self,op):
        self.op=getop(op)

    def apply(self,left,right):
        return self.op(left,right)


class InterpolatingFunction(Function):
    def __init__(self,x,y,lower,high):
        self.x=x
        self.y=y
        self.low=lower
        self.high=high

    def apply(self,x):
        if x<=self.high or x>=self.low:
            return nev.neville(self.x,self.y,x)
        else:
            raise er.OutofSpecifiedRangeError

    def graph(self):
        plt.plot(self.x,self.y)
        plt.ylabel('y(x)')
        plt.xlabel('x')
        plt.show()


class StringFunction(Function):
    def __init__(self, string):  # string with variable x in it
        self.string = str(string)
        try:
            self.string.index('x')
        except (IndexError, ValueError):
            raise er.FunctionVariableInputError

    def apply(self, x):
        x = x
        return ne.evaluate(self.string)  # uses x value

    def __str__(self):
        return self.string


