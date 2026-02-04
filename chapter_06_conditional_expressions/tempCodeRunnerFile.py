
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
d=int(input("Enter a number: "))

if (a > b and c and d):
    print("This number is greater -> ",a)
if (b > a and c and d):
    print("This number is greater -> ",b)
if (c > b and a and d):
    print("This number is greater -> ",c)
if (d > b and c and a):
    print("This number is greater -> ",d)