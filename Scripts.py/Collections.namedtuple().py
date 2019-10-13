from collections import namedtuple
n=int(input())
m=(input().split())
indice_voto=m.index('MARKS')
Student= namedtuple('Student','MARKS')
voti_totali=[]
for elem in range(n):
    studente=(list(input().split()))
    studente=Student(studente[indice_voto])
    voti_totali+=[studente.MARKS]
voti_totali=list(map(float,voti_totali))
average=(sum(voti_totali))/n
print('%.2f'%average)
