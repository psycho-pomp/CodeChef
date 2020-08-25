# cook your dish here
t=int(input())
for _ in range(t):
    s=(input())
    res="YES"
    if s[0]!=s[1]:
        for i in range(len(s)):
            if i%2==0:
                if s[i]!=s[0]:
                    res="NO"
            else:
                if s[i]!=s[1]:
                    res="NO"
        print(res)
    else:
        print("NO")
                
