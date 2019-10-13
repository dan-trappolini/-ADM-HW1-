from collections import Counter
import re
stringa=input()
caratteri=(re.findall('[a-zA-Z]{1}',stringa))
caratteri.sort()
risultato=(Counter(caratteri).most_common(3))
for elem in risultato:
    print(*elem)
