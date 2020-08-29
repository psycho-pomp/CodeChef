# cook your dish here
def addZeros(strr, n): 
    for i in range(n): 
        strr = "0" + strr 
    return strr 
t=int(input())
for _ in range(t):
    a,b=input().split()
    aLen = len(a) 
    bLen = len(b) 
    if (aLen > bLen): 
        b = addZeros(b, aLen - bLen) 
    elif (bLen > aLen): 
        a = addZeros(a, bLen - aLen) 
    l=max(aLen,bLen)
    #print(a,b)
    res=""
    for i in range(l):
        #print(a[i],b[i])
        res+=str(int(a[i])+int(b[i]))[-1]
    print(int(res))
        
