# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    nc=0
    ne=0
    no=0
    nd=0
    nh=0
    nf=0
    for i in range(n):
        s=input()
        s.lower()
        nc+=s.count("c")
        ne+=s.count("e")
        no+=s.count("o")
        nd+=s.count("d")
        nh+=s.count("h")
        nf+=s.count("f")
    x=min(no,nh,nd,nf)
    y=min(nc,ne)//2
    print(min(x,y))
        
        
        
