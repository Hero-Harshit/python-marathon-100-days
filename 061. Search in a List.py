# Search in a List
# Ask the user for an element and check if it exists in the list.

items = ["apple", "banana", "cherry", "date"]
print(f"Current items: {items}")

target = input("Enter an item to search for: ")

if target in items:
    print(f"Yes, '{target}' is in the list.")
else:
    print(f"No, '{target}' is not in the list.")
