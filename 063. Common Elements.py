# Common Elements
# Take two lists and create a list containing values that appear in both lists.

list1 = input("Enter first list items (separated by spaces): ").split()
list2 = input("Enter second list items (separated by spaces): ").split()

common = []
for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print(f"Common elements: {common}")
