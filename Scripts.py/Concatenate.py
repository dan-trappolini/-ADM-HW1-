import numpy
n=list(map(int,input().split()))
N=n[0]
M=n[1]
P=n[2]
matrix_1=numpy.array([input().strip().split() for i in range(N)],int)
matrix_2=numpy.array([input().strip().split() for i in range(M)],int)
print (numpy.concatenate((matrix_1, matrix_2), axis = 0))
