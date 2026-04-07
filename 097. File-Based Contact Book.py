# File-Based Contact Book
# Build a contact-book program that stores contact information in a file and supports adding, searching, updating, and deleting contacts.
import os

FILENAME = "contacts.txt"

def load_contacts():
    contacts = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    contacts[parts[0]] = parts[1]
    return contacts

def save_contacts(contacts):
    with open(FILENAME, "w") as f:
        for name, phone in contacts.items():
            f.write(f"{name},{phone}\n")

contacts = load_contacts()

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View All")
    print("3. Search Contact")
    print("4. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        save_contacts(contacts)
        print("Contact added.")
    elif choice == '2':
        if not contacts:
            print("No contacts found.")
        else:
            for n, p in contacts.items():
                print(f"{n}: {p}")
    elif choice == '3':
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"Found: {name} -> {contacts[name]}")
        else:
            print("Not found.")
    elif choice == '4':
        break
    else:
        print("Invalid choice.")
