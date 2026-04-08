# JSON Student Database
# Store student records in a JSON file and create functions to add, search, update, delete, and display students.

import json
import os

FILENAME = "students.json"

def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_data(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

db = load_data()

while True:
    print("\n--- JSON Student Database ---")
    print("1. Add Student")
    print("2. View All")
    print("3. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        grade = input("Enter Grade: ")
        db[roll_no] = {"name": name, "grade": grade}
        save_data(db)
        print("Student added successfully.")
    elif choice == '2':
        if not db:
            print("Database is empty.")
        else:
            for r, info in db.items():
                print(f"Roll No: {r} | Name: {info['name']} | Grade: {info['grade']}")
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
