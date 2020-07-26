# cook your dish he
n=int(input())

c=list(map(int,input().split()))
t=list(map(int,input().split()))
#print(c,t)
min_t,min_a,min_at=1000000,1000000,1000000
for i in range(n):
    if t[i]==1:
        min_t=min(c[i],min_t)
    elif t[i]==2:
        min_a=min(c[i],min_a)
    elif t[i]==3:
        min_at=min(c[i],min_at)
#print(min_at,min_a,min_t)
print(min((min_a+min_t),min_at))
