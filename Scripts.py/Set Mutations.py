n=int(input())
S=set(map(int,input().split()))
n_comandi=int(input())
comandi = {'intersection_update' : S.intersection_update,'update' : S.update,'symmetric_difference_update' : S.symmetric_difference_update,'difference_update':S.difference_update}
L=[]
for i in range(n_comandi):
    L=input().split()
    comando=L[0] 
    argomento=list(map(int,input().split()))
    comandi[comando](argomento)
print(sum(S))
