# cook your dish here
t=int(input())
for _ in range(t):
    s=input()
    sa,sb=map(int,input().split())
    n=(s.index("B")-s.index("A"))%(sa+sb)
    if n!=0:
        #print((s.index("B")-s.index("A")+1)/(sa+sb))
        print("safe")
    else:
        print("unsafe")
    
