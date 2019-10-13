A=set(map(int,input().split()))
n=int(input())
L=[]
for elem in range(n):
    subset=set(map(int,input().split()))
    if A==subset:
        L+=[False]
    elif subset.issubset(A)==False:
        L+=[False]
    else:
        L+=[True]
if False in L:
    print('False')
else:
    print('True')
