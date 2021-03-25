T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    if X%2==0:
        if (X//2)<=Y:
            print(X//2)
    else:
        if (X//2)<Y:
            print(X//2)
