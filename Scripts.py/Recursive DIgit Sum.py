def superDigit(n, k=1):
    from functools import reduce
    N=str(n)
    if len(N)==1:
        return(n)
    else:
        lista=[]
        for elem in N:
            lista+=[elem]
        lista=list(map(int,N))
        return superDigit(reduce((lambda x,y:x+y),lista*k))
