# Replace a Word
# Find a specific word in a string and replace it with another word.

text = input("Enter a sentence: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

if old_word in text:
    updated_text = text.replace(old_word, new_word)
    print(f"Updated sentence: {updated_text}")
else:
    print(f"'{old_word}' was not found in the sentence.")
