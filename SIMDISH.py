t=int(input())
for _ in range(t):
    d1=set(input().split())
    d2=set(input().split())
    if len(d1.intersection(d2))>=2:
        print("similar")
    else:
        print("dissimilar")
