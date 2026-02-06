
class programmer:
   name="Name"
   age=int(25)
   salary=int(200000)
   company = "Microsoft" 
   def __init__(self,name,age,salary):
      self.name=name
      self.age=age
      self.salary=salary
      
  


a = programmer("ali",22,300000)
b = programmer("kamran",27,350000)
c = programmer("safwan",30,150000)

print(a.name)
print(a.age)
print(a.salary)
print(a.company)
print()
print(b.name)
print(b.age)
print(b.salary)
print(b.company)
print()
print(c.name)
print(c.age)
print(c.salary)
print(c.company)
 