
word="unique"
with open("04_paragraph.txt") as f:
    content=f.read()


if word in content:
    print(f"The word {word}  is present in the text.")
else:
    print(f"The word {word}  is not present in the text.")
