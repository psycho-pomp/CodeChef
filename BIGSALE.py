# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    loss=0
    for i in range(n):
        price,quantity,discount=map(int,input().split())
        increased_price=((100+discount)*price)/100
        discounted_price=(increased_price*(100-discount))/100
        loss+=quantity*(price-discounted_price)
    print(loss)
