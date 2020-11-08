def findlog(p):
    x=0
    while p!=0:
        x+=1
        p//=2
    return x-1
f=[0,1]
for i in range(2,61):
    f.append((f[i-1]+f[i-2])%10)
#print(f)
t=int(input())
for _ in range(t):
    n=int(input())
    t=findlog(n)
    ind=(2**t)-1
    idx=int(ind%60)
    print(f[idx])
