# cook your dish here
x,y=map(float,input().split())
x=int(x)
if x%5==0 and x+0.50<=y:
    y=y-x-0.50
print(y)
