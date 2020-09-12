from collections import Counter
# cook your dish here\

n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
res=-1
a.sort()
d=Counter(a)
x=sum(d.values())
for i in d:
    res=max(res,x*i)
    x-=d[i]
print(res)
        
