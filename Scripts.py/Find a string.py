def count_substring(string, sub_string):
    contatore=0
    l_1=len(string)
    l_2=len(sub_string)
    for i in range (0,(l_1-l_2)+1):
        try :
            if string[i:i+len(sub_string)]==sub_string:
                contatore +=1
        except IndexError : break

    return(contatore)
        
