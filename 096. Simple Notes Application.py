# Simple Notes Application
# Create a program that lets the user add notes to a file and later display all saved notes.

filename = "notes.txt"

while True:
    print("\n1. Add a note")
    print("2. View all notes")
    print("3. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        note = input("Enter your note: ")
        with open(filename, "a") as f:
            f.write(note + "\n")
        print("Note added!")
    elif choice == '2':
        try:
            with open(filename, "r") as f:
                print("\n--- Saved Notes ---")
                print(f.read())
                print("-------------------")
        except FileNotFoundError:
            print("No notes found yet.")
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
