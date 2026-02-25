# Remove Duplicates
# Remove all duplicate values from a list while keeping the original order.

user_input = input("Enter items separated by spaces: ")
items = user_input.split()

unique_items = []
for item in items:
    if item not in unique_items:
        unique_items.append(item)

print(f"List without duplicates: {unique_items}")
