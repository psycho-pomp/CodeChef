# cook your dish here
def nCr(n, r): 
  
    return (fact(n) / (fact(r)  
                * fact(n - r))) 
  
# Returns factorial of n 
def fact(n): 
  
    res = 1
      
    for i in range(2, n+1): 
        res = res * i 
          
    return res 
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    k_smallest=l[:k]
    y=k_smallest.count(k_smallest[-1])
    cntx=l.count(k_smallest[-1])
    print(int(nCr(cntx,y)))
    
