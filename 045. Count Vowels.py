# Count Vowels
# Count how many vowels (a, e, i, o, u) are in a string.

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"The string contains {count} vowel(s).")
