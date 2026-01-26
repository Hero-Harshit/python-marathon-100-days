# Reverse a Number
# Take an integer and reverse it using a loop or string manipulation.

num = input("Enter an integer to reverse: ")
if num.startswith("-"):
    reversed_num = "-" + num[:0:-1]
else:
    reversed_num = num[::-1]

print(f"The reversed number is: {reversed_num}")
