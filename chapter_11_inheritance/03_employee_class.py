
class employee:
    salary=200
    increment=20
    @property
    def salaryafterincrement(self):
        return(self.salary+self.salary*(self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment=((salary/self.salary) -1)*100
    


e=employee()
e.salaryafterincrement=270
print("Increment is ",e.increment)
print("Salary after increment is ",e.salaryafterincrement)
