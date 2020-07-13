# cook your dish here
#do not declare max and min in if case as it increases time complexity
n,q=map(int,input().split())
a=list(map(int,input().split()))
Max=max(a)
Min=min(a)
for _ in range(q):
    t=int(input())
    if t<=Max and t>=Min:
        print("Yes")
    else:
        print("No")
    
