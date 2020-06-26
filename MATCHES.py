t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    x=n+m
    d={'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}
    c=0
    for i in str(x):
        #print(i,d[i])
        c+=d[i]
    print(c)
