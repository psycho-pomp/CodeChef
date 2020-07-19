# cook your dish here
t=int(input())
for _ in range(t):
    s,w1,w2,w3=map(int,input().split())
    if w1+w2+w3<=s:
        print(1)
    elif w1+w2<=s:
        print(2)
    elif w1<=s:
        if w2+w3<=s:
            print(2)
        else:
            print(3)
