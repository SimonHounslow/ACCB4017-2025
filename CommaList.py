# Get comma-separated input from the user
user_input = input("Enter a list of items, separated by commas: ")

# Split the string into a list using comma as separator
items = user_input.split(',')

print(f"{len(items)} items total")


# Print each item on a new line
for item in items:
    print(item.strip())  # .strip() removes extra spaces