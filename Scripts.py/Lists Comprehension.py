if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    from itertools import product
    print([list(p) for p in product(range(x + 1), range(y + 1), range(z + 1)) if sum(p) != n])

