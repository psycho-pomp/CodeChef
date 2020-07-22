# cook your dish here
t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    
    
    if (l[1]>l[0] and l[4]>l[3]) or (l[1]<l[0] and l[4]<l[3]) or (l[1]==l[0] and l[4]==l[3]): 
        if (l[2]>l[1] and l[5]>l[4]) or (l[2]<l[1] and l[5]<l[4]) or (l[2]==l[1] and l[5]==l[4]):
            if (l[2]>l[0] and l[5]>l[3]) or (l[2]<l[0] and l[5]<l[3]) or (l[2]==l[0] and l[5]==l[3]):
                print("FAIR")
            else:
                print("NOT FAIR")
        else:
            print("NOT FAIR")
    else:
        print("NOT FAIR")
