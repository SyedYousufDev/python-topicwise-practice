
num=int(input("Enter a number:-> "))
factorial=1

for i in range (2,num+1):
  if(num==0 or num==1):
    print(f"The factorial of {i} is 1.")
  else:
   factorial*=i

print(f"The factorial of {i} is {factorial}.")
