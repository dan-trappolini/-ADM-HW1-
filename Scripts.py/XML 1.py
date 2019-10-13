def get_attr_number(node):
    import xml.etree.ElementTree as etree
    tree = etree.ElementTree(etree.fromstring(xml))
    L=[]
    for elem in tree.iter():
        L+=[len(elem.items())]
    return(sum(L))
