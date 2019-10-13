from collections import OrderedDict
n=int(input())
ordered_dictionary = OrderedDict()
for elem in range(n):
    shop=(input().split())
    shop=shop[::-1]
    price=int(shop[0])
    item=(shop[1:])
    item=item[::-1]
    item=' '.join(item)
    if item in ordered_dictionary:
        ordered_dictionary[item]=ordered_dictionary[item]+price
    else:
        ordered_dictionary[item]=price
for elem in ordered_dictionary:
    print (elem,ordered_dictionary[elem])
