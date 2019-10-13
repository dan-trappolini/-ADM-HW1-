string=input()
A=[]
B=[]
D=[]
E=[]
F=[]
for c in string:
    a=c.isalnum()
    A+=[a]
if True in A:
    print('True')
else:
    print('False')
for c in string:
    b=c.isalpha()
    B+=[b]
if True in B:
    print('True')
else:
    print('False')
for c in string:
    d=c.isdigit()
    D+=[d]
if True in D:
    print('True')
else:
    print('False')
for c in string:
    e=c.islower()
    E+=[e]
if True in E:
    print('True')
else:
    print('False')
for c in string:
    f=c.isupper()
    F+=[f]
if True in F:
    print('True')
else:
    print('False')
        
