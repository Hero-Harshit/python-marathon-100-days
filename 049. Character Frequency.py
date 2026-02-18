# Character Frequency
# Ask the user for a string and count the frequency of every character.

text = input("Enter a string: ")
freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character Frequencies:")
for char, count in freq.items():
    # Use repr() to make spaces and special chars visible
    print(f"{repr(char)}: {count}")
