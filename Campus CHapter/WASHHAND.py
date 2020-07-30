import sys
input=sys.stdin.readline
def main():
    T=int(input())
    for _ in range(T):
        N=int(input())
        if (T<=100 and N<=2000):
            S=input()
            val=int(S,2)
            D=int(input())
            P=list(map(int,input().split()))
            yu=(1<<N)-1
            r=0
            l=0
            for i in range(D):
                p=P[i]
                r=r|1<<(N-p+1)
                l=l|1<<(N-p)
                val1=val>>1&(~l)&yu
                val2=val<<1&(~r)&yu
                val=(val|val1|val2)&yu
                #print(bin(val),bin(r),bin(l))
                
            y=bin(val).count('1')
            print(y)
        else:
            S=input()
            val=int(S,2)
            D=int(input())
            P=list(map(int,input().split()))
            yu=(1<<N)-1
            r,l=0,0
            for i in range(D):
                p=P[i]
                #r=r|1<<(N-p+1)
                l=l|1<<(N-p)
                val1=val>>1&(~l)&yu
                val2=val<<1&yu
                val=(val|val1|val2)&yu
                #print(bin(val),bin(r),bin(l))
            y=bin(val).count('1')
            print(str(y)+"\n")
main()        
        
    
    
        
        
        
    
    
        
        
