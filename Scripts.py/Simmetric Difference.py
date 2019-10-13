m=input()
M=set(map(int,(input().split())))
n=input()
N=set(map(int,(input().split())))
risultato=M^N
risultato=sorted(risultato)
for elem in risultato:
    print(elem)
