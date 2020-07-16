# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    if a==d and b==c:
        print("YES")
    elif a==c and b==d:
        print("YES")
    elif a==b and c==d:
        print("YES")
    else:
        print("NO")
