# cook your dish here
t=int(input())
for _ in range(t):
    salary=int(input())
    if salary<1500:
        gross_salary=salary+(salary*0.9)+(salary*0.1)
    else:
        gross_salary=salary+500+(0.98*salary)
    print(gross_salary)
