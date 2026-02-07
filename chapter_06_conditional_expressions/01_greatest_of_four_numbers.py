

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
d=int(input("Enter a number: "))

if a > b and a > c and a > d:
    print("This number is greater ->", a)
elif b > a and b > c and b > d:
    print("This number is greater ->", b)
elif c > a and c > b and c > d:
    print("This number is greater ->", c)
elif d > a and d > b and d > c:
    print("This number is greater ->", d)
