from numpy import *
n, m = map(int, input().split())
array = array([input().strip().split() for i in range(n)], int)
print (array.transpose())
print (array.flatten())
