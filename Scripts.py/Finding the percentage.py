n=int(input('inserisci numero: ')) #numero di studenti 
key=[]
values=[]
for i in range(n):
    s=input('inserisci studente e voti: ' ).split() #metto il nome e i voti in una lista
    key+=[s[0]]
    s=s[1:]
    s=list(map(float,s))
    values+=[s]
dizionario={k:v for (k,v) in zip(key,values)}
nome_studente=input('inserisci un nome: ')
risultato= dizionario[nome_studente]
R=sum(risultato)
N=len(risultato)
results=R/N
results='%4.2f' %results
print(results)
    

    
    

    
