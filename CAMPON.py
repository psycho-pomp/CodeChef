# cook your dish here
t=int(input())
for _ in range(t):
    D=int(input())
    date=[0]*32
    for i in range(D):
        d,p=map(int,input().split())
        date[d]=p
    Q=int(input())
    for i in range(Q):
        dead,req=map(int,input().split())
        if req<=sum(date[:dead+1]):
            print("Go Camp")
        else:
            print("Go Sleep")
            
            
    
