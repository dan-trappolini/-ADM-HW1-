import re
risultato=(re.findall('[aeiouAEIOU]{2,}',input()))
if len(risultato)!=0:
    for elem in risultato:
        print(elem)
else:
    print(-1)
