# cook your dish here
t=int(input())
for _ in range(t):
    c,d,l=map(int,input().split())
    max_l=(c+d)*4
    if 2*d>=c:
        min_l=d*4
    else:
        min_l=(c-d)*4
    if min_l<=l<=max_l and (l-min_l)%4==0:
        print("yes")
    else:
        print("no")
        
