
text="this text has  double space."

index=text.find("  ")
print(index)

is_doublespace_present="  " in text
print(is_doublespace_present)

text1="this text doesnot have double space."

index1=text1.find("  ")
print("\nThe second text not have space in it so answer is following.\n",index1)

is_doublespace_present1="  " in text1
print(is_doublespace_present1)