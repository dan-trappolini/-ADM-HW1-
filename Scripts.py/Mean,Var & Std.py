import numpy
n=(input().split())
n=list(map(int,n))
N=n[0]
M=n[1]
matrix= numpy.array([(list(map(int,input().split())))for i in range(N)])
numpy.set_printoptions(legacy='1.13')
print (numpy.mean(matrix, axis = 1))
print (numpy.var(matrix, axis = 0)) 
print (numpy.std(matrix, axis = None))
