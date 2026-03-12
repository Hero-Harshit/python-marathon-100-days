# Student Dictionary
# Create a dictionary storing a student's name, age, course, and marks.

student = {
    "name": input("Enter student's name: "),
    "age": input("Enter student's age: "),
    "course": input("Enter student's course: "),
    "marks": input("Enter student's marks: ")
}

print("\nStudent Details:")
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")
