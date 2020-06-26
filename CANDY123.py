t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    i=1
    limak=0
    bob=0
    while(True):
        if i%2!=0:
            limak+=i
            #print(limak)
        else:
            bob+=i
            #print(bob)
        if limak>a:
            #print(limak)
            print("Bob")
            break
        elif bob>b:
            #print(bob)
            print("Limak")
            break
        i+=1
