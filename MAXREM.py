# cook your dish here
n=int(input())
l=list(map(int,input().split()))
m=max(l)
res=-1
for i in l:
    res=max(res,i%m)
print(res)
