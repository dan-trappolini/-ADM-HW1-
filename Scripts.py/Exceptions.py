n=int(input())
for elem in range(n):
    try:
        i=list(map(int,input().split()))
        numeratore=i[0]
        denominatore=i[1]
        risultato=(numeratore/denominatore)
        print(int(risultato))
    except ZeroDivisionError as e:
        print ("Error Code: integer division or modulo by zero")
    except ValueError as f:
        print('Error Code:',f)
