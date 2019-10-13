import numpy
n=int(input())
matrix=numpy.array([input().split()for i in range(n)],float)
numpy.set_printoptions(legacy='1.13')
print(numpy.linalg.det(matrix)) 
