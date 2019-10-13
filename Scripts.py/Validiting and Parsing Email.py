import re
n=int(input())
for i in range(n):
    l=input().split()
    check=l[1]
    pattern=r'<[a-zA-Z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>'
    risultato=re.match(pattern,check)
    if risultato !=None:
        print(*l)
    
