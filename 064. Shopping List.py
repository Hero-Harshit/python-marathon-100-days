# Shopping List
# Create a program that allows the user to add items, remove items, and display their shopping list.

shopping_list = []

while True:
    print("\n--- Shopping List Menu ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"'{item}' added.")
    elif choice == '2':
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed.")
        else:
            print(f"'{item}' not found in the list.")
    elif choice == '3':
        print("\nCurrent Shopping List:")
        if not shopping_list:
            print("(Empty)")
        else:
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
