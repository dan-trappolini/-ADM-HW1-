import numpy
n=list(map(int,input().split()))
N=n[0]
M=n[1]
matrix=numpy.array([input().split()for i in range(N)],int)
n_matrix=(numpy.min(matrix, axis = 1))
print (numpy.max(n_matrix))
