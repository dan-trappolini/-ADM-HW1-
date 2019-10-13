import numpy
n=list(map(int,input().split()))
N=n[0]
A=numpy.array([input().split()for i in range(N)],int)
B=numpy.array([input().split()for i in range(N)],int)
print (numpy.dot(A, B)) 
