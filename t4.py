n = int(input('введите Ваше число:'))
m=0
while n>=10:
    e=(n%10)
    if e>m:
        m=e
    else: m=m
    n=n//10
e=(n%10)
if e>m:
    m=e
else: m=m
print (f"самая большая цифра числа: {m}")