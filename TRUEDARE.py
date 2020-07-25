# cook your dish here
# cook your dish here
t=int(input())
for _ in range(t):
    ntr=int(input())
    tr=set(map(int,input().split()))
    ndr=int(input())
    dr=set(map(int,input().split()))
    nts=int(input())
    ts=set(map(int,input().split()))
    nds=int(input())
    ds=set(map(int,input().split()))
    if len(ts.difference(tr))==0 and len(ds.difference(dr))==0:
        print("yes")
    else:
        print("no")
