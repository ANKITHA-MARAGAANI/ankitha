n=in=int(input())
for for i in range(n):
    for j in range(n):
        if ((i==0)or((j==0)and(i<=n//2))or(i==n//2)|((j==n-1)&(i>=n//2))|(i==n-1)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
