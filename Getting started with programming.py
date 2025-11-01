birthdays = {}  # empty dictionary

for i in range(5):
    name = input("Enter your friend's name: ")
    date = input("Enter their birthday (DD-MM-YYYY): ")
    birthdays[name] = date

print("\n--- Birthdays of Raj's friends ---")
for name, date in birthdays.items():
    print(f"{name}: {date}")