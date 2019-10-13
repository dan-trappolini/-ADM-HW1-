T = int(input())
for elem in range(T):
    n_A = int(input())
    A = set(map(int,input().split()))
    n_B = int(input())
    B = set(map(int,input().split()))
    print (bool(A.issubset(B)))
