import numpy
Pol=list(map(float,input().split()))
x=float(input())
print (numpy.polyval(Pol, x))
