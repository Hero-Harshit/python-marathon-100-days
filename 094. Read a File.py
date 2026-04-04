# Read a File
# Read a text file and display its complete contents on the terminal.

filename = input("Enter the filename to read (e.g., my_note.txt): ")
try:
    with open(filename, "r") as file:
        content = file.read()
        print("\n--- File Content ---")
        print(content)
        print("--------------------")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
