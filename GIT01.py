# cook your dish here
t=int(input())
for _ in range(t):
    r,c=map(int,input().split())
    c1,c2=0,0
    for i in range(r):
        s=input()
        if i%2==0:
            for j in range(c):
                if j%2==0: 
                    if s[j]!='R':
                        c1+=3
                    elif s[j]!='G':
                        c2+=5
                elif j%2!=0:
                    if s[j]!='G':
                        c1+=5
                    elif s[j]!='R':
                        c2+=3
        else:
            for j in range(c):
                if j%2==0: 
                    if s[j]!='R':
                        c2+=3
                    elif s[j]!='G':
                        c1+=5
                elif j%2!=0:
                    if s[j]!='G':
                        c2+=5
                    elif s[j]!='R':
                        c1+=3
    print(min(c1,c2))
            
    
