def kangaroo(x1, v1, x2, v2):
    for e1,e2 in zip(range(x1,100000000,v1),range(x2,100000000,v2)):
        if e1==e2:
            return ('YES')
            break
    return ('NO')
