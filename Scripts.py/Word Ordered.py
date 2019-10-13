from collections import OrderedDict
n=int(input())
L=[]
for elem in range(n):
    s=input()
    L+=[s]
ordered_dictionary = OrderedDict()
for elem in range(n):
    elem=L[elem]
    if elem in ordered_dictionary:
        ordered_dictionary[elem]=ordered_dictionary[elem]+1
    else:
        ordered_dictionary[elem]=1
n_elementi=len(set(L))
print(n_elementi)
for elem in ordered_dictionary:
    print (ordered_dictionary[elem],sep=' ',end=' ')
