# Merge Two Lists
# Take two lists and combine them into a single list.

list1 = input("Enter items for the first list (separated by spaces): ").split()
list2 = input("Enter items for the second list (separated by spaces): ").split()

merged = list1 + list2
print(f"Merged List: {merged}")
