
f=open("01_poem.txt")
content =f.read()
if("Twinkle" in content):
    print("Twinkle is present in poem")
else:
    print("Twinkle is not present")
f.close()
