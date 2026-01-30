from datetime import date
Date= date.today()
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 

print(letter.replace("<|Name|>","Yousuf").replace("<|Date|> ",str(Date)))