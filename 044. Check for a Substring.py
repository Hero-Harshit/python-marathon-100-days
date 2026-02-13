# Check for a Substring
# Check if a shorter string exists within a longer string.

main_string = input("Enter the main string: ")
substring = input("Enter the substring to look for: ")

if substring in main_string:
    print("The substring exists within the main string.")
else:
    print("The substring does not exist in the main string.")
