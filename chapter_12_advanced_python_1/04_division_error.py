# try_except problem
num=int(input("Enter a integer: "))
num2=int(input("Enter a second integer: "))

try:
    print(f"The division num1/num2 is {num/num2}")
except Exception as e:
    print("The second number can't be zero.")    