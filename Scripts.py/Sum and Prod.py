n=list(map(int,input().split()))
N=n[0]
M=n[1]
matrix=numpy.array([input().split()for i in range(N)],int)
n_matrix=(numpy.sum(matrix, axis = 0))
print (numpy.prod(n_matrix))
