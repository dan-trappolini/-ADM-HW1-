from functools import reduce
def wrap(string, max_width):
    lunghezza=len(string)
    S=[]
    for elem in range(0,lunghezza,max_width):
        s=(string[elem:elem+max_width])
        S+=[s]+['\n']
    risultato=reduce((lambda x,y:x+y),S)
    return risultato