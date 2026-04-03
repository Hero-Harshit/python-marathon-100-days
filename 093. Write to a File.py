# Write to a File
# Ask the user for a note and save it into a text file.

note = input("Enter a note to save: ")
try:
    with open("my_note.txt", "w") as file:
        file.write(note)
    print("Note saved to 'my_note.txt' successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
