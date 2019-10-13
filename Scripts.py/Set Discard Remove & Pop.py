n=int(input())
S=set(map(int,input().split()))
n_comandi=int(input())
comandi = {'pop' : S.pop,'remove' : S.remove,'discard' : S.discard}
L=[]
for i in range(n_comandi):
    L=input().split()
    comando=L[0] 
    if comando!='pop':
        argomento=L[1]
        argomento=int(argomento)
        comandi[comando](argomento)
    else:
        comandi[comando]()
print(sum(S))
