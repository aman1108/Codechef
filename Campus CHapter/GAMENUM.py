import math
def rR(n, d,INT_BITS):  
    return ((n >> d)|(n << (INT_BITS - d))&((1<<INT_BITS)-1))

T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    v=n^m
    fc=0
    if (n>m):
        INT_BITS=int(math.log2(n)+1)
    else:
        INT_BITS=int(math.log2(m)+1)
    for i in range(1,INT_BITS):
        #print(rR(m,i,INT_BITS))
        a=(rR(m,i,INT_BITS)^n)
        if (a>v):
            v=a
            fc=i
    print(fc,v)
        
