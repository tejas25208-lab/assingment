# Start the program
# We want to arrange clothes in an almirah

# Step 1: Take clothes details
# Each cloth has: name, category, and how often it is used

clothes = [
    ("Shirt", "Formal", "High"),
    ("Jeans", "Casual", "High"),
    ("Kurta", "Traditional", "Medium"),
    ("Blazer", "Formal", "Low"),
    ("T-Shirt", "Casual", "Medium"),
    ("Sherwani", "Traditional", "Low")
]

# Step 2: Create shelves in the almirah
# Middle shelf = most used
# Upper shelf = medium used
# Lower shelf = least used

middle_shelf = []
upper_shelf = []
lower_shelf = []

# Step 3: Arrange clothes one by one
for cloth in clothes:

    name = cloth[0]        # cloth name
    category = cloth[1]    # cloth type
    usage = cloth[2]       # usage frequency

    # If cloth is used daily, keep in middle shelf
    if usage == "High":
        middle_shelf.append(name + " (" + category + ")")

    # If cloth is used sometimes, keep in upper shelf
    elif usage == "Medium":
        upper_shelf.append(name + " (" + category + ")")

    # If cloth is rarely used, keep in lower shelf
    else:
        lower_shelf.append(name + " (" + category + ")")

# Step 4: Display final arrangement
print("Almirah Arrangement")

print("\nMiddle Shelf (Most Used Clothes):")
print(middle_shelf)

print("\nUpper Shelf (Medium Used Clothes):")
print(upper_shelf)

print("\nLower Shelf (Least Used Clothes):")
print(lower_shelf)

# End of program