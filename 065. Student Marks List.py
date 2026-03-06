# Student Marks List
# Store marks of multiple students in a list and print each student's marks along with the class average.

marks = []
while True:
    user_input = input("Enter a student's marks (or type 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        mark = float(user_input)
        marks.append(mark)
    except ValueError:
        print("Please enter a valid number.")

if not marks:
    print("No marks entered.")
else:
    total = sum(marks)
    average = total / len(marks)
    
    print("\n--- Student Marks ---")
    for i, m in enumerate(marks, 1):
        print(f"Student {i}: {m}")
    print(f"Class Average: {average:.2f}")
