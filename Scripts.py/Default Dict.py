from collections import defaultdict
d = defaultdict(list)
a=list(map(int,input().split()))
n=a[0]
m=a[1]
for i in range(n):
    d[input()].append(i+1)
C=[]
for i in range(m):
    c=input()
    C+=[c]
for elem in C:
    if elem in d:
        print(*d[elem])
    else:
        print(-1)
