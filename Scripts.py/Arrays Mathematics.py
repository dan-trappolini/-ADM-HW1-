import numpy
n=list(map(int,input().split()))
N=n[0]
M=n[1]
A=numpy.array([input().strip().split()for i in range(N)],int)
B=numpy.array([input().strip().split()for i in range(N)],int)
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)
