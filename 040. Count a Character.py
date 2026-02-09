# Count a Character
# Ask the user for a string and a character, and count how many times that character appears.

text = input("Enter a string: ")
char_to_find = input("Enter the character to count: ")

if len(char_to_find) == 1:
    count = text.count(char_to_find)
    print(f"The character '{char_to_find}' appears {count} time(s).")
else:
    print("Please enter exactly one character to count.")
