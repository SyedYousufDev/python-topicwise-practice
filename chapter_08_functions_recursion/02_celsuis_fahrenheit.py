

def C_F(cel):
 F = (cel*(9/5)) + 32
 return F


print("Enter temprature in Celcuis: ")
cel=float(input())

f=C_F(cel)
print("Your given temprature in farhenheit is ",f)