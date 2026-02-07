# String Slicing
# Extract and print a specific portion of a string.

text = input("Enter a string: ")
try:
    start = int(input("Enter start index: "))
    end = int(input("Enter end index: "))
    
    sliced = text[start:end]
    print(f"Sliced string: '{sliced}'")
except ValueError:
    print("Invalid input. Indices must be integers.")
