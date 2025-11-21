# Example of working with a dictionary in Python

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Updating a value
my_dict["age"] = 26  # Update the age

# Displaying the updated dictionary
print("Updated dictionary:", my_dict)

# Two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

# /// Merging Two Lists into a Dictionary in Python 

# Creating an empty dictionary
my_dict = {}

# Merging lists into dictionary using a loop
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

# Displaying the dictionary
print("Merged dictionary:", my_dict)

