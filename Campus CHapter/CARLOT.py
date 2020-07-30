T=int(input())
for _ in range(T):
    M,N=map(int,input().split())
    c=0
    cp=-1
    v=0
    s=M
    for i in range(M):
        A=list(map(str,input().split()))
        if (((i+1)%2)!=0):
            for j in range(N):
                if (A[j]=='P'):
                    v=i
                    if (cp!=-1):
                        c=c+abs(cp-j)
                    cp=j
                    s=min(i,s)
        else:
            for j in range(N-1,-1,-1):
                if (A[j]=='P'):
                    v=i
                    if (cp!=-1):
                        c=c+abs(cp-j)
                    cp=j
                    s=min(i,s)
        #print(c,cp,s,v)
    print(max(c+v-s,0))
