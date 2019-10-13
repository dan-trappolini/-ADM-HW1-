import re
def wrapper(f):
    def fun(l):
        Risultato=[]
        for number in l:
            pattern=re.compile('([0|91|\+91])*([0-9]{5})([0-9]{5})')
            risultato=re.sub(pattern, r"+91 \2 \3", number)
            risultato=risultato.strip()
            Risultato+=[risultato]
        Risultato.sort()
        print(*Risultato,sep='\n')
    return fun
