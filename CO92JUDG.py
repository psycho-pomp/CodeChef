t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    sa=sum(a)-max(a)
    sb=sum(b)-max(b)
    if sa>sb:
        print("Bob")
    elif sb>sa:
        print("Alice")
    else:
        print("Draw")
