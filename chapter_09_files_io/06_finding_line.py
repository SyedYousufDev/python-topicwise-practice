
word = "unique"

with open("04_paragraph.txt") as f:
    line_no = 1
    for line in f:
        if word in line:
            print(f"The word '{word}' is present on line {line_no}")
        line_no += 1