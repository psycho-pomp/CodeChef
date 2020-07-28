# cook your dish here]\\
t=int(input())
for _ in range(t):
    s=input()
    c=0
    for i in range(len(s)-3):
        if 'c' in s[i:i+4] and 'h' in s[i:i+4] and 'e' in s[i:i+4] and 'f' in s[i:i+4]:
            c+=1
    if c!=0:
        print("lovely",c)
    else:
        print("normal")
