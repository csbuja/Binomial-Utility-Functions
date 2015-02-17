import math

def nCr(n,r):
    f=math.factorial
    return f(n) / f(r) / f(n-r)

def atLeast(numTrials,atLeast,p):
    p = float(p)
    total = 0.0
    while atLeast<=numTrials:
            total += (nCr(numTrials,atLeast)*p**atLeast*((1-p)**(numTrials-atLeast)))
            atLeast+=1
    return total


def atMost(numTrials,max,p):
    return 1.0 - atLeast(numTrials,max+1,p)


print atMost(3,2,.5)