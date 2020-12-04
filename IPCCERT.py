# cook your dish here
n,m,k=map(int,input().split())
count=0
for i in range(n):
    l=list(map(int,input().split()))
    s=sum(l)-l[k]
    if s>=m and l[k]<=10:
        #print(s,l[k])
        count+=1
print(count)
