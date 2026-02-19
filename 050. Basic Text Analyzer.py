# Basic Text Analyzer
# Take a paragraph and display its number of characters, words, spaces, uppercase letters, lowercase letters, and digits.

text = input("Enter a paragraph: ")

chars = len(text)
words = len(text.split())
spaces = text.count(" ")
uppercase = sum(1 for c in text if c.isupper())
lowercase = sum(1 for c in text if c.islower())
digits = sum(1 for c in text if c.isdigit())

print("--- Text Analysis ---")
print(f"Total Characters: {chars}")
print(f"Total Words: {words}")
print(f"Spaces: {spaces}")
print(f"Uppercase Letters: {uppercase}")
print(f"Lowercase Letters: {lowercase}")
print(f"Digits: {digits}")
