L=[]
Score_list=[]
risultati=[]
n=int(input())
for elem in range(n):
    name=input()
    score=(int(input())
    L+=[[name,score]]
    Score_list+=[score]
minimo=min(Score_list)
for i in range(n):
    if minimo==min(Score_list):
        Score_list.remove(min(Score_list))
secondo_minimo=min(Score_list)
for elem in L:
    if secondo_minimo in elem:
        risultati+=elem
print(risultati[0])
