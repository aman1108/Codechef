mod=10**9+7
def mI(a, m) : 
      
    g = gcd(a, m) 
      
    if (g != 1) : 
        print("Inverse doesn't exist") 
          
    else : 
          
        # If a and m are relatively prime, 
        # then modulo inverse is a^(m-2) mode m 
        return(power(a, m - 2, m))
                                    
      
# To compute x^y under modulo m 
def power(x, y, m) : 
      
    if (y == 0) : 
        return 1
          
    p = power(x, y // 2, m) % m 
    p = (p * p) % m 
  
    if(y % 2 == 0) : 
        return p  
    else :  
        return ((x * p) % m) 
  
# Function to return gcd of a and b 
def gcd(a, b) : 
    if (a == 0) : 
        return b 
          
    return gcd(b % a, a)

def gcd(a, b) : 
    if (a == 0) : 
        return b 
          
    return gcd(b % a, a) 

T=int(input())
mv=10**9
Q=mI(pow(52,mv,mod),mod)
for _ in range(T):
    N,K=map(int,input().split())
    P=0
    for i in range(N):
        L=int(input())
        c=pow(52,mv-L,mod)
        b=pow((2*K+52),(L//2),mod)
        
        if (L==1):
            P=52
        elif (L%2==0):
            P=(b)%(1000000007)
        else:
            P=(b*52)%(1000000007)
        #print(P)
        print((P*Q*c)%(mod))
