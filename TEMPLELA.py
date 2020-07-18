# cook your dish here
s=int(input())
for _ in range(s):
    n=int(input())
    a=list(map(int,input().split()))
    result='yes'
    if n%2==0:
        result="no"
    else:
        if a[0]!=1:
            result="no"
        elif a[n-1]!=1:
            result="no"
        else:
            center=n//2
            for i in range(1,center+1):
                if a[i]-a[i-1]!=1:
                    result='no'
                    break
            for i in range(center,n-1):
                if a[i]-a[i+1]!=1:
                    result='no'
                    break
    print(result)
                    
                
            
            
            
        
