
def sum_by_recursion(n):
    if n == 0:
        return 0
    sum=n+sum_by_recursion(n-1)
    return sum



n=int(input("Enter a number to find sum of its natural numbers."))
s=sum_by_recursion(n)
print("Sum of N numbers is ",s)