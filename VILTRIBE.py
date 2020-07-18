# cook your dish here
t=int(input())
for _ in range(t):
    s=input()
    flag=''
    a=0
    b=0
    x=0
    for i in s:
        if i=='A':
            a+=1
            if flag=='A':
                a+=x
                
            else:
                flag='A'
            x=0
            
        elif i=='B':
            b+=1
            if flag=="B":
                b+=x
                
            else:
                flag='B'
            x=0
            
        elif i=='.':
            x+=1
    print(a,b)
        
