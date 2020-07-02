# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    l=list(s)
    i=0
    while i+1<n:
        l[i],l[i+1]=l[i+1],l[i]
        i+=2
    print(''.join(chr(122 - ord(c) + 97) for c in l))
