# Phone Book
# Build a simple dictionary-based phone book where users can add, search, update, and delete contacts.

phone_book = {}

while True:
    print("\n--- Phone Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All")
    print("6. Exit")
    
    choice = input("Enter choice (1-6): ")
    
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        phone_book[name] = phone
        print(f"Contact '{name}' added.")
    elif choice == '2':
        name = input("Enter name to search: ")
        if name in phone_book:
            print(f"{name}: {phone_book[name]}")
        else:
            print("Contact not found.")
    elif choice == '3':
        name = input("Enter name to update: ")
        if name in phone_book:
            phone = input("Enter new phone number: ")
            phone_book[name] = phone
            print(f"Contact '{name}' updated.")
        else:
            print("Contact not found.")
    elif choice == '4':
        name = input("Enter name to delete: ")
        if name in phone_book:
            del phone_book[name]
            print(f"Contact '{name}' deleted.")
        else:
            print("Contact not found.")
    elif choice == '5':
        if not phone_book:
            print("Phone book is empty.")
        else:
            for name, phone in phone_book.items():
                print(f"{name}: {phone}")
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
