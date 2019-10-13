import re
n=int(input())
testo=[]
for i in range(n):
    testo+=[input()]
for elem in testo:
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$',elem)))
