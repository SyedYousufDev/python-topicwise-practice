
comment=str(input("Enter a comment: "))
comment=comment.lower()

keyword_1 = "make a lot of money"
keyword_2 = "buy now"
keyword_3 = "subscribe this"
keyword_4 = "click this"
#comment 3
if((keyword_1 in comment) or (keyword_2 in comment) or (keyword_3 in comment) or (keyword_4 in comment) ):
  print("The comment you typed is  spam.Thank you")
else:  
  print("The comment you typed is not spam.Thank you")