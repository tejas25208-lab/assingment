# Start the program
# We want to pack clothes in a luggage bag for a 7-day trip

# Step 1: Take trip clothing details
# Each item has: name, activity type, usage priority, and delicacy

items = [
    ("T-Shirts", "Sightseeing", "High", "Normal"),
    ("Jeans", "Sightseeing", "High", "Normal"),
    ("Hiking Shoes", "Hiking", "High", "Heavy"),
    ("Jacket", "Hiking", "Medium", "Normal"),
    ("Formal Shirt", "Dinner", "Medium", "Delicate"),
    ("Formal Pants", "Dinner", "Medium", "Delicate"),
    ("Sleepwear", "Daily", "High", "Normal"),
    ("Accessories", "Daily", "Low", "Normal")
]

# Step 2: Create sections in the luggage bag
# Top section = easy access items
# Middle section = regular clothes
# Bottom section = heavy or less used items
# Side pouch = delicate items

top_section = []
middle_section = []
bottom_section = []
side_pouch = []

# Step 3: Arrange items one by one
for item in items:

    name = item[0]          # item name
    activity = item[1]      # activity type
    priority = item[2]      # usage priority
    delicacy = item[3]      # delicacy level

    # If item is delicate, place in side pouch for protection
    if delicacy == "Delicate":
        side_pouch.append(name + " (" + activity + ")")

    # If item is used daily, keep in top section
    elif priority == "High":
        top_section.append(name + " (" + activity + ")")

    # If item is used sometimes, keep in middle section
    elif priority == "Medium":
        middle_section.append(name + " (" + activity + ")")

    # If item is heavy or rarely used, keep at bottom
    else:
        bottom_section.append(name + " (" + activity + ")")

# Step 4: Display final packing arrangement
print("Luggage Packing Arrangement")

print("\nTop Section (Easy Access Items):")
print(top_section)

print("\nMiddle Section (Regular Clothes):")
print(middle_section)

print("\nBottom Section (Heavy / Less Used Items):")
print(bottom_section)

print("\nSide Pouch (Delicate Items):")
print(side_pouch)

# End of program
