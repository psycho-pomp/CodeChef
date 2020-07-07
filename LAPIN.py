t=int(input())
for _ in range(t):
    s=input()
    x=list(s[:len(s)//2])
    x.sort()
    if len(s)%2==0:
        y=list(s[len(s)//2:])
    else:
        y=list(s[((len(s)//2)+1):])
    y.sort()
    
    if x==y:
        print("YES")
    else:
        print("NO")
