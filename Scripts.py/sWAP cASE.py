from functools import reduce
def swap_case(s):
    S=[]
    s.replace(' ','/')
    for elem in s:
        if elem.islower()==True:
            elem=elem.capitalize()
            S.append(elem)
        else:
            elem=elem.lower()
            S.append(elem)
    R=reduce((lambda x,y:x+y),S)
    R=R.replace('/',' ')
    return(R)
        
            
            
        
        