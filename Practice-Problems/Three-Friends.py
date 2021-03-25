T = int(input())
for _ in range(T):
    x,y,z=map(int, input().split())
    if (x==y) and (y==z) and z==x:
        print('no')
    else:
        print('yes')