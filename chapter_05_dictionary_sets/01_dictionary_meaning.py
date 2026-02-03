
urdu_to_english = {
    "mohabbat": "Love",
    "dost": "Friend",
    "kitab": "Book",
    "pani": "Water",
    "ghar": "Home",
    "maa": "Mother",
    "baap": "Father",
    "school": "School",
    "kaam": "Work",
    "khushi": "Happiness"
}

#Printing all words
print("You can search for these words: ")
for word in urdu_to_english:
    print("-",word)

#search for the word 
search=input("\nEnter a word:")

#dictionay meaning of the word
meaning=urdu_to_english.get(search.lower(),"Word Not Found!")
print("Meaning:",meaning)


