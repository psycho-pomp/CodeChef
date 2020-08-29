# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    if c==d and abs(b-a)!=0:
        print("NO")
    elif c==d and abs(b-a)==0:
        print("YES")
        
    elif abs(b-a)%(abs(c-d))==0:
        print("YES")
    else:
        print("NO")
