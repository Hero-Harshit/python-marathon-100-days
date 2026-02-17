# Palindrome String
# Check if a string reads the same forwards and backwards.

text = input("Enter a string: ")
# Remove spaces and convert to lowercase for a better check
cleaned_text = text.replace(" ", "").lower()

if cleaned_text == cleaned_text[::-1]:
    print(f"'{text}' is a palindrome!")
else:
    print(f"'{text}' is NOT a palindrome.")
