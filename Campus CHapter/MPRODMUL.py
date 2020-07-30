T=int(input())
D={1:[1],2:[2,1],3:[3,1],4:[4,2,1],5:[5,1],6:[6,3,2,1],7:[7,1],8:[8,4,2,1],9:[9,3,1]}
for _ in range(T):
    A,B,K=map(int,input().split())
    A=A+(K-(A%K))
    c=0
    fv=-1
    for i in range(A,B+1,K):
        v=str(i)
        flag=0
        c1=1
        for j in range(len(v)-1):
            for k in range(j+1,len(v)):
                if (int(v[k])==0):
                    flag=1
                    break
                if ((int(v[j])%int(v[k]))==0):
                    flag=0
                    break
                else:
                    flag=1
            if(flag==1):
                c1=0
                break
            else:
                c1=c1*int(v[j])
        #print(i,c1)
        c1=c1*int(v[len(v)-1])
        if (c1>c):
            c=c1
            fv=i
    if(c==0):
        print(-1)
    else:
        print(c,fv)
            
    
