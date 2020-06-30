# cook your dish here
n=int(input())
m,c=map(int,input().split())
l=0
r=0
for _ in range(n):
    x,y,p=map(int,input().split())
    if y<(m*x)+c:
        l+=p
    else:
        r+=p
print(max(l,r))
