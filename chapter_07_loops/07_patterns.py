'''n=3
  *
 *** 
*****
'''
num=int(input("Enter a number:-> "))

for i in range(1,num+1):
    print(" "*(num-i),end="")
    print("*"*(2*i-1),end="")
    print()

''' n=3
*
*** 
***** 
'''
for i in range(1,num+1):
    print("*"*(2*i-1),end="")
    print()

''' n=3
    *
  *** 
***** 
'''

print()
for i in range(num,0,-1):
    print(" "*(num-i),end="")
    print("*"*(2*i-1),end="")
    print()



''' n=3
*****    
*** 
* 
'''
print()
for i in range(num,0,-1):
    print("*"*(2*i-1),end="")
    print()

''' n=3
*****    
*   * 
*****    
'''
print()
for i in range(1,num+1):
    if(i==1 or i==num):
        print("*"*num,end="")
    else:
        print("*",end="")
        print(" "*(num-2),end="")
        print("*",end="")
    print()    