# Build a CLI Python Calculator
# Build a complete terminal-based calculator with a menu, arithmetic operations, powers, percentage calculations, input validation, exception handling, calculation history stored in a file, and a command to clear the history.

import os

HISTORY_FILE = "calc_history.txt"

def add_history(record):
    with open(HISTORY_FILE, "a") as f:
        f.write(record + "\\n")

def view_history():
    if os.path.exists(HISTORY_FILE):
        print("\\n--- Calculation History ---")
        with open(HISTORY_FILE, "r") as f:
            print(f.read())
    else:
        print("\\nNo history found.")

def clear_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        print("History cleared.")
    else:
        print("No history to clear.")

while True:
    print("\\n--- CLI Calculator Menu ---")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Percentage (%)")
    print("7. View History")
    print("8. Clear History")
    print("9. Exit")
    
    choice = input("Enter your choice (1-9): ")
    
    if choice in ['1', '2', '3', '4', '5', '6']:
        try:
            num1 = float(input("Enter first number: "))
            
            if choice == '6':
                print("Percentage is calculated as (num1 / 100) * num2")
                
            num2 = float(input("Enter second number: "))
            
            result = 0
            op = ""
            if choice == '1':
                result = num1 + num2
                op = "+"
            elif choice == '2':
                result = num1 - num2
                op = "-"
            elif choice == '3':
                result = num1 * num2
                op = "*"
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
                op = "/"
            elif choice == '5':
                result = num1 ** num2
                op = "^"
            elif choice == '6':
                result = (num1 / 100) * num2
                op = "% of"
            
            record = f"{num1} {op} {num2} = {result}"
            print(f"\\nResult: {record}")
            add_history(record)
            
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            
    elif choice == '7':
        view_history()
    elif choice == '8':
        clear_history()
    elif choice == '9':
        print("Exiting CLI Calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please select from 1-9.")
