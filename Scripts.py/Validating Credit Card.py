import re
n=int(input())
for i in range(n):
    credit_card=input()
    pattern=(r"^[5|4|6]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$")
    R=re.match(pattern,credit_card)
    if '-' in credit_card:
        n_credit_card=credit_card.replace('-','')
        pattern_0='[1]{4}|[2]{4}|[3]{4}|[4]{4}|[5]{4}|[6]{4}|[7]{4}|[8]{4}|[9]{4}'
        risultato=re.findall(pattern_0,n_credit_card)
    else:
        n_credit_card=credit_card
        pattern_0='[1]{4}|[2]{4}|[3]{4}|[4]{4}|[5]{4}|[6]{4}|[7]{4}|[8]{4}|[9]{4}'
        risultato=re.findall(pattern_0,n_credit_card)
    if R!=None and (len(risultato)<1):
        print('Valid')
    else:
        print('Invalid')
