def minion_game(s):
    import re
    l=len(s)
    kevin_score=0
    stuart_score=0
    for i in range(l):
        pattern='[aeiouAEIOU]'
        risultato=re.match(pattern,s[i:])
        if risultato!=None:
            kevin_score+=(l-i)
        else:
            stuart_score+=(l-i)
    if kevin_score==stuart_score:
        print('Draw')
    elif kevin_score>stuart_score:
        print('Kevin',kevin_score)
    else:
        print('Stuart',stuart_score)

