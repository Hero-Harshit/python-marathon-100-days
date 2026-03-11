# Word Set
# Take a sentence and create a set containing every unique word in it.

sentence = input("Enter a sentence: ")
# Convert to lowercase to ignore case differences
words = sentence.lower().split()

unique_words = set(words)
print(f"Unique words: {unique_words}")
