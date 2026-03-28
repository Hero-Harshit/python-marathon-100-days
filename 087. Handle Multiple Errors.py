# Handle Multiple Errors
# Create a program that safely handles invalid input, division by zero, and missing dictionary keys.

data = {"a": 10, "b": 20, "c": 0}

try:
    key1 = input("Enter first key (a, b, c): ")
    key2 = input("Enter second key (a, b, c): ")
    
    val1 = data[key1]
    val2 = data[key2]
    
    result = val1 / val2
    print(f"Result of division: {result}")
    
except KeyError as e:
    print(f"Error: Key {e} not found in dictionary.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print(f"Unexpected error: {e}")
