# cook your dish here
t=int(input())
for _ in range(t):
    n=(input())
    s=n.count("s")
    m=n.count("m")
    i=0
    while i<len(n)-1:
        if n[i:i+2]=='sm' or n[i:i+2]=='ms':
            s-=1
            i=i+2
        else:
            i=i+1
    if s>m:
        print("snakes")
    elif m>s:
        print("mongooses" )
    else:
        print("tie")
