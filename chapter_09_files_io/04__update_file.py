#A file contains a word “Donkey” multiple times. You need to write a program 
#which replace this word with ##### by updating the same file.  

with open("04_paragraph.txt","r") as f:
    p=f.read()

update=p.replace("Donkey","#####")  

with open("04_paragraph.txt","w") as f:
    p=f.write(update)      