def LPS(pat, M, lps): 
    len = 0 
    lps[0]
    i = 1
    while (i < M): 
        if pat[i]== pat[len]: 
            len += 1
            lps[i] = len
            i += 1
        else: 
            if (len != 0): 
                len = lps[len-1] 
            else: 
                lps[i] = 0
                i += 1

                
T=int(input())
for _ in range(T):
    X=int(input())
    N=int(input())
    A=list(map(int,input().split()))
    M=int(input())
    B=list(map(int,input().split()))
    D=[]
    R=[]
    P=[]
    fc=0
    if (N==1):
        for i in range(M):
            if (abs(B[i]-A[0])<=X):
                fc=fc+1
        print(fc)
    else:
        for i in range(N-1):
            D.append(A[i+1]-A[i])
        lps=[0 for i in range(len(D))]
        LPS(D,len(D),lps)
        for i in range(M-1):
            R.append(B[i+1]-B[i])
        i=0
        j=0

        #print(D)
        M=len(D)
        N=len(R)
        while(i<N):
            if (R[i]==D[j]):
                i=i+1
                j=j+1

            if (j==M):
                P.append(i-j)
                j=lps[j-1]
    
            elif(i<N and D[j]!=R[i]):
                if (j!=0):
                    j=lps[j-1]
                else:
                    i=i+1

            #print(P)
        for i in P:
            if (abs(A[0]-B[i])<=X):
                fc=fc+1
        print(fc)
                
    

    
                    
            
