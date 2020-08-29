# cook your dish her
def Odd_days(x,n):
    odd_days=0
    for i in range(x,n):
        if (i%4==0 and i%100!=0 ) or i%400==0:
            odd_days+=2
        else:
            odd_days+=1
    return odd_days
    
day=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
t=int(input())
for _ in range(t):
    n=int(input())
    if n>=2001:
        odd_days=Odd_days(2001,n)
        odd_days%=7
        req=(odd_days+1)%7
    else:
        odd_days=Odd_days(n,2001)
        odd_days%=7
        req=(1-odd_days)%7
    
    
    print(day[req])
