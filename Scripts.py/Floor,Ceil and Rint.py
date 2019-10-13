import numpy
n=list(map(float,input().split()))
n_array=numpy.array(n)
numpy.set_printoptions(sign=' ')
print (numpy.floor(n_array))
print (numpy.ceil(n_array))
print (numpy.rint(n_array)) 

