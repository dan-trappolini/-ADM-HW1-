n=int(input())
i=5
Like=[]
for elem in range(0,n):
    p=(math.floor(i/2))
    like=p
    i=p*3
    Like+=[like]
print(sum(Like))
