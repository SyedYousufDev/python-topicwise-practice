#String are immutable
text="this text  has  double  space."

print("Before cleaning->\n",text)
#After replacing double spaces so 
print("\n\"After cleaning the text\"")
cleaned_text=text.replace("  "," ")
print(cleaned_text)
