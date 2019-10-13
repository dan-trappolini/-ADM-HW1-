import numpy
def arrays(arr):
    arr=arr[::-1]
    arr=list(map(float,arr))
    return(numpy.array(arr))
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
