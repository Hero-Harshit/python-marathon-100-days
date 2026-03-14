# Update Dictionary
# Create a student dictionary and allow the user to update one of its values.

student = {"name": "John Doe", "age": 20, "grade": "B"}
print(f"Current Dictionary: {student}")

key_to_update = input("Which key would you like to update? ")
if key_to_update in student:
    new_value = input(f"Enter new value for {key_to_update}: ")
    student[key_to_update] = new_value
    print(f"Updated Dictionary: {student}")
else:
    print("That key does not exist.")
