m=input()
M=set(map(int,(input().split())))
n=input()
N=set(map(int,(input().split())))
risultato=M|N
risultato=set(risultato)
res=len(risultato)
print(res)
