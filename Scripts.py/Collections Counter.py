import collections

n = int(input())
shoes = collections.Counter(map(int,input().split()))
clienti = int(input())

totale = 0

for i in range(clienti):
    comprato = list(map(int,input().split()))
    size=comprato[0]
    price=comprato[1]
    if shoes[size]: 
        totale += price
        shoes[size] -= 1

print (totale)
