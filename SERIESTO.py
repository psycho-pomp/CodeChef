def addZeros(strr, n): 
    for i in range(n): 
        strr = "0" + strr 
    return strr 
def getXNOR(a, b):
    aLen = len(a) 
    bLen = len(b) 
    if (aLen > bLen): 
        b = addZeros(b, aLen - bLen) 
    elif (bLen > aLen): 
        a = addZeros(a, bLen - aLen) 
    lenn = max(aLen, bLen)
    res = "" 
    for i in range(lenn): 
        if (a[i] != b[i]): 
            res += "0"
        else: 
            res += "1"
    res="0b"+res
    return res 
    
t=int(input())
for _ in range(t):
    a,b,n=map(int,input().split())
    xor=0
    xnor=0
    if n%3==0:
        xor=a^b
        x=bin(a).replace("0b", "") 
        y=bin(b).replace("0b", "")
        xnor=int(getXNOR(x,y),2)
        print(max(xor,xnor))
    elif n%3==1:
        print(a)
    elif n%3==2:
        print(b)
