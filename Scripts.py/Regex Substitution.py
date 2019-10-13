import re

for i in range(int(input())):
        s = input()
        s = re.sub(r" \&\&(?= )", " and", s)
        s = re.sub(r" \|\|(?= )", ' or', s)
        print(s)
