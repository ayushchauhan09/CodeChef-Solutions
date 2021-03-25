X, Y = input().split()
if int(X)<float(Y) and int(X)%5==0:
    print(float(Y)-int(X)-0.50)
else:
    print(float(Y))