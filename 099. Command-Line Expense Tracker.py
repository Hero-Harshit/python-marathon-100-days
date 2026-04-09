# Command-Line Expense Tracker
# Create a CLI expense tracker where the user can add expenses, view all expenses, calculate the total, filter by category, and save the data to a JSON file.

import json
import os

FILENAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            try:
                return json.load(f)
            except:
                return []
    return []

def save_expenses(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

expenses = load_expenses()

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total")
    print("4. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        desc = input("Enter description: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., Food, Travel): ")
        expenses.append({"desc": desc, "amount": amount, "category": category})
        save_expenses(expenses)
        print("Expense added.")
    elif choice == '2':
        for idx, exp in enumerate(expenses, 1):
            print(f"{idx}. {exp['desc']} | ${exp['amount']} | {exp['category']}")
    elif choice == '3':
        total = sum(exp['amount'] for exp in expenses)
        print(f"Total Expenses: ${total:.2f}")
    elif choice == '4':
        break
    else:
        print("Invalid choice.")
