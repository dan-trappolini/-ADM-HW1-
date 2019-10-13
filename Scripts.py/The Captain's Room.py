from collections import Counter
n=int(input()) #numero di ospiti per stanza
stanze=list(map(int,input().split()))
dizionario=Counter(stanze)
K=[]
V=[]
for elem in(dizionario.keys()):
    K+=[elem]
for elem in(dizionario.values()):
    V+=[elem]

n_dizionario={k:v for (k,v) in zip (V,K)}
print(n_dizionario[(min(n_dizionario))])
