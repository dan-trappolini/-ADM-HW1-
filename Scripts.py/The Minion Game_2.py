def count_substring(string, sub_string):
    return(sum([1 for i in range(0, len(string) - len(sub_string) + 1) if (string[i:(len(sub_string)+i)] == sub_string)]))


def minion_game(string):
    player_1='Stuart' #può iniziare solo con consonanti
    player_2='Kevin' #può iniziare solo con vocali
    lista_player_1=[]
    lista_player_2=[]
    L=[]
    lunghezza=len(string)
    for elem in string:
        L+=[elem]
    L=set(L)
    i=0
    R=[]
    while i<lunghezza:
        for i_2 in range(0,6):
            for elem in range(i_2,lunghezza+1,(lunghezza-i)):
                r=string[elem-(lunghezza-i):elem]
                R+=[r]
        i+=1
    R=set(R)
    R.remove('')
    R=list(R)
    for elem in R:
        if elem.startswith('A') or elem.startswith('E') or elem.startswith('I') or elem.startswith('O') or elem.startswith('U'):
            lista_player_2+=[elem]
        else:
            lista_player_1+=[elem]
    score_1=[]
    score_2=[]
    for elem in lista_player_1:
        score=count_substring(string,elem)
        score_1+=[score]
    for elem in lista_player_2:
        score=count_substring(string,elem)
        score_2+=[score]
    print(score_1)
    print(score_2)
    print(lista_player_1)
    print(lista_player_2)
    final_score_1=sum(score_1)
    final_score_2=sum(score_2)
    if final_score_1==final_score_2:
        print('Draw')
    elif max(final_score_1,final_score_2)==final_score_1:
        print(player_1,final_score_1)
    else:
        print(player_2,final_score_2)



