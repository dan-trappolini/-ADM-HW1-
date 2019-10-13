import re
n=int(input())
for i in range(n):
    number=input()
    check=(re.match(r'[789]\d{9}$',number))
    if check!=None:
        print('YES')
    else:
        print('NO')

