def insertionSort1(n, arr):
    L=arr
    c=arr[-1]
    arr=arr[:-1]
    Maggiori=list(filter((lambda x:x>c),arr))
    Minori=list(filter((lambda x:x<=c),arr))
    Maggiori=Maggiori[::-1]
    for elem in Maggiori:
        arr.append(elem)
        arr.sort()
        print(*arr)
        arr.remove(elem)
    for elem in Minori:
        L.sort()
        print(*L)
