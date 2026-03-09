# Remove Duplicates Using a Set
# Take a list with repeated values and use a set to obtain unique values.

user_input = input("Enter items with duplicates (separated by spaces): ")
items_list = user_input.split()

# Convert list to set to remove duplicates, then back to list
unique_items = list(set(items_list))

print(f"Original list: {items_list}")
print(f"Unique items: {unique_items}")
