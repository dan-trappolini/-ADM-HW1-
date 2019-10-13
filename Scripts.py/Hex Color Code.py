import re
n=int(input())
txt=input()
pattern=re.compile(r'[:](#)([1234567890a-fA-F]{3,6})')
result=re.findall(pattern,txt)
for elem in result:
    print(*elem)
