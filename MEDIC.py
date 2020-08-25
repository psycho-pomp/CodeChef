month={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
t=int(input())

for _ in range(t):
    yyyy,mm,dd=map(int,input().split(":"))
    res=month[mm]
    if mm==2 and (yyyy%400==0 or (yyyy%4==0 and yyyy%100!=0)):
        res=29
    if res%2==0:
        res+=month[(mm+1)]
    print((res-dd+2)//2)
