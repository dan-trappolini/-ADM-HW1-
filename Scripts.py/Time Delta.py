n=int(input())
from datetime import datetime as dt
x='%a %d %b %Y %H:%M:%S %z'
for i in range(n):
    y=(dt.strptime(input(), x))
    z=(dt.strptime(input(),x))
    risultato=(int(abs((y-z).total_seconds())))
    print(risultato)
