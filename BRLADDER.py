# cook your dish here
q=int(input())
for _ in range(q):
    a,b=map(int,input().split())
    if a>b:
        a,b=b,a
    if a%2==1 and (b==a+1 or b==a+2):
        
        print("YES")
    elif a%2==0 and b==a+2:
        print("YES")
    else:
        print("NO")
    
