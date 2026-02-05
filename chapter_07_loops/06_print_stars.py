n=9
i=1

while (i<=n):
    j=1
    while(j<=i):
      print("*",end=" ")
      j=j+1
    print()  
    i=i+1  
      
print() 

n=9 
i=1
while (i<=n):
    j=9
    while(j>=i):
      print("*",end=" ")
      j=j-1
    print()  
    i=i+1 
n=9
i=1

while (i<=n):
    j=1
    while(j<=i):
      print("*",end=" ")
      j=j+1
    print()  
    i=i+1  

print()
n=9
i=n

while (i>=1):
    space=n-i
    j=0
    while(j< space ):
      print(" ",end="")
      j=j+1
    k=0
    while (k<i):  
      print("*",end=" ")  
      k+=1
    print()
    i=i-1     