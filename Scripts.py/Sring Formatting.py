def print_formatted(n):
    l=len('{0:b}'.format(n))
    for elem in range(1,n+1):
        print ("{0:{l}d} {0:{l}o} {0:{l}X} {0:{l}b}".format(elem,l=l))
if __name__ == '__main__':
