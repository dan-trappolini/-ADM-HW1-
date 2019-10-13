n=int(input())
f=n
l=[]
i=1
while i!=0:
    i=n
    l+=[n]
    n=n-1
l=l[:-1]
l.sort()
for i in l:
    print(i,sep='',end='')
