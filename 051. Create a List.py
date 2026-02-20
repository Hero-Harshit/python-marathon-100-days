# Create a List
# Create a list of 5 fruits, ask the user to input a new fruit, and append it to the list.

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"Current list of fruits: {fruits}")

new_fruit = input("Enter a new fruit to add: ")
fruits.append(new_fruit)

print(f"Updated list of fruits: {fruits}")
