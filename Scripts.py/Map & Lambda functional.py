cube = lambda x:x**3
def fibonacci(n):
    L=[]
    for i in range(n):
        p=my_fibonacci(i)
        L+=[p]
    return L
    
def my_fibonacci(n):
    if n <= 1:
        return n
    else:
        return (my_fibonacci(n-1) + my_fibonacci(n-2))
    
