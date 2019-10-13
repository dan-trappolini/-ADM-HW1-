def solve(s):
    string=s.split(' ')
    risultato=[]
    for elem in string:
        elem=elem.capitalize()
        risultato+=[elem]
    return(' '.join(risultato))
