# First and Last Character
# Print the first and last characters of a user-entered string.

text = input("Enter a string: ")
if text:
    print(f"First character: {text[0]}")
    print(f"Last character: {text[-1]}")
else:
    print("The string is empty.")
