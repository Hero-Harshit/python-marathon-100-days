# File Statistics
# Read a text file and report the number of lines, words, and characters it contains.

filename = input("Enter the filename to analyze: ")
try:
    with open(filename, "r") as file:
        lines = file.readlines()
        
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
        
        print(f"\nStatistics for {filename}:")
        print(f"Lines: {num_lines}")
        print(f"Words: {num_words}")
        print(f"Characters: {num_chars}")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
