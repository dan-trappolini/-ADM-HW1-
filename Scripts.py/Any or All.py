n=int(input())
N=input().split()
N_l=[]
for elem in N:
    if int(elem)>0:
        N_l+=[int(elem)]
    else:
        N_l+=[0]
if all(N_l)>0:
    x=True
else:
    x=False
N_p=[]
for elem in N:
    j=elem[::-1]
    if elem==j:
        N_p+=[int(elem)]
    else:
        N_p+=[0]
if any(N_p)>0:
    y=True
else:
    y=False
risultato=x and y
print(risultato)
