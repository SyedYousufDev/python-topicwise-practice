"""" Write a program to find out whether a student has passed or failed 
if it requires a total of 40% and at least 33% in each subject to pass. 
Assume 3 subjects and take marks as an input from the user."""

sub1=int(input("Enter Marks of 1st Subject obtained/50: "))
sub2=int(input("Enter Marks of 2nd Subject obtained/50: "))
sub3=int(input("Enter Marks of 3rd Subject obtained/50: "))

per_1= (sub1/50)*100
per_2= (sub2/50)*100
per_3= (sub3/50)*100

per_total= ((per_1+per_2+per_3)/300)*100

print(per_1,per_2,per_3,per_total)

if (per_1>=33 and per_2>=33 and per_3>=33):
    if(per_total>=40):
     print("Congrugalations ! You have passed.KEEP IT UP.")
    else:
       print("Sorry! You have failed.GOOD LUCK for next time.")
else:
   print("Sorry! You have failed.GOOD LUCK for next time.")       
        