# Count Words
# Count the number of words in a sentence entered by the user.

text = input("Enter a sentence: ")
# split() with no arguments splits by any whitespace
words = text.split()
print(f"The sentence contains {len(words)} word(s).")
