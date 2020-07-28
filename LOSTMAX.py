# cook your dish here
t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    l.remove(len(l)-1)
    print(max(l))
