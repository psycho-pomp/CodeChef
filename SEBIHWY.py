# cook your dish here
t=int(input())
for _ in range(t):
    s,sg,fg,d,t=map(int,input().split())
    so=s+((d*50*18)/(t*5))
    xs=abs(so-sg)
    xf=abs(so-fg)
    if xs<xf:
        print("SEBI")
    elif xf<xs:
        print("FATHER")
    else:
        print("DRAW")
    
