# cook your dish here
n,k=map(int,input().split())
open=[]
for _ in range(k):
    l=list(input().split())
    if len(l)==2:
        if l[1] in open:
            open.remove(l[1])
        elif l[1] not in open:
            open.append(l[1])
    elif len(l)==1:
        open=[]
    print(len(open))
