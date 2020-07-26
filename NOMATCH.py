# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    print(sum(l[:n//2])-sum(l[n//2:]))
