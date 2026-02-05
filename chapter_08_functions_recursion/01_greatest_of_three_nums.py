n1=n2=n3=0
def great(n1,n2,n3):
    if (n1>n2 and n1>n3):
        print("The greatest number is ",n1)
    if (n2>n1 and n2>n3):
        print("The greatest number is ",n2)
    if (n3>n2 and n3>n1):
        print("The greatest number is ",n3)        


print("Enter three numbers to find its greatest:")
n1=input()
n2=input()
n3=input()

great(n1,n2,n3)