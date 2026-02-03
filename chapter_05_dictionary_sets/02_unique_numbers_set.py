
unique_numbers=set()

num=0
for i in range(7):
  num=input(f"\nEnter the {i+1}. number: ")
  
  unique_numbers.add(num)
  
print(unique_numbers)  
print(type(unique_numbers))