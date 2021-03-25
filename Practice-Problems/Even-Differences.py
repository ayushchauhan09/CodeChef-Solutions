T = int(input())
for _ in range(T):
    a = int(input())
    arr = map(int, input().split())
    if sum(arr)%2==0:
        print(0)
    else:
        print(1)