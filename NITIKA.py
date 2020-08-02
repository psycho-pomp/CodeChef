# cook your dish here
t=int(input())
for _ in range(t):
    l=input().split()
    length=len(l)
    if length==1:
        print(l[0].capitalize())
    elif length==2:
        print(l[0][0].upper()+". "+l[1].capitalize())
    else:
        print(l[0][0].upper()+". "+l[1][0].upper()+". "+l[2].capitalize())
        
