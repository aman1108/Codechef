T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    a=max(A)
    b=max(B)
    if (a!=b):
        print("YES")
    else:
        print("NO")
