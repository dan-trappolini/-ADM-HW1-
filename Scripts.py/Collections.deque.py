from collections import deque
n=int(input())
d=deque()
comandi={'append':d.append,'appendleft':d.appendleft,
         'pop':d.pop,'popleft':d.popleft}
for elem in range(n):
    s=input().split()
    comando=s[0]
    if len(s)==1:
        comandi[comando]()
    else:
        argomento=int(s[1])
        comandi[comando](argomento)
for elem in d:
    print(elem,sep=' ',end=' ')
