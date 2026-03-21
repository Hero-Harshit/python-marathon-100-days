# String Utility Functions
# Create functions for reversing a string, counting vowels, and counting words.

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def count_words(s):
    return len(s.split())

text = input("Enter a string: ")
print(f"Reversed: {reverse_string(text)}")
print(f"Vowel count: {count_vowels(text)}")
print(f"Word count: {count_words(text)}")
