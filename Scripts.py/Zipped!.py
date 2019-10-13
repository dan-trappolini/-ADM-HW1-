n=list(map(int,input().split()))
n_studenti=n[0] 
n_voti=n[1] 
lista=[list(map(float,input().split()))for i in range(n_voti)]
for i in zip(*lista):
    print( sum(i)/n_voti) 
