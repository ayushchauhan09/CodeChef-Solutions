T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 1
    x = list()
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1])<=2:
            count += 1
            x.append(count)
        else:
            count = 1
    print(x)