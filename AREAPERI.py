# cook your dish here
l=int(input())
b=int(input())
if l*b>2*(l+b):
    print("Area")
    print(l*b)
elif 2*(l+b)>(l*b):
    print("Peri")
    print(2*(l+b))
else:
    print("Eq")
    print(l*b)
