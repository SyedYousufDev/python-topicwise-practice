
#The following is calculator which do the 4 basic calculation...It is implemented using python classes
class calculator():
    num1=int(0)
    num2=int(0)
    opr=str("+")
    
    def add(self,num1,num2):
        return num1+num2
    def sub(self,um1,num2):
        return num1-num2    
    def mul(self,num1,num2):
        return num1*num2
    def div(self,num1,num2):
        if(num2==0):
           print("Invalid question")
        else:   
         return num1/num2

num1=num2=0
opr="o"
st="yes"
while(st=="yes"):
  my_cal=calculator()
  print("Enter the two numbers and operator between them numm1,num2,operator")
  num1=int(input())
  num2=int(input())
  opr=input()
  if(opr=="+"):
    print("Your answer is this: ", my_cal.add(num1,num2))
  if(opr=="-"):
    print("Your answer is this: ", my_cal.sub(num1,num2))
  if(opr=="*"):
    print("Your answer is this: ", my_cal.mul(num1,num2))  
  if(opr=="/"):
    print("Your answer is this: ", my_cal.div(num1,num2))
  st = input("Do you want to continue? (yes/no): ")