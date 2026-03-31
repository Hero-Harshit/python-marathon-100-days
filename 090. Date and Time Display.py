# Date and Time Display
# Use Python's datetime module to display the current date, current time, and day of the week.

import datetime

now = datetime.datetime.now()

print(f"Current Date: {now.strftime('%Y-%m-%d')}")
print(f"Current Time: {now.strftime('%H:%M:%S')}")
print(f"Day of the Week: {now.strftime('%A')}")
