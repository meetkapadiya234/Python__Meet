# Example of using the math module in Python

# Importing the math module
import math

# Taking a number as input
num = float(input("Enter a number: "))

# Using math.sqrt() to find square root
square_root = math.sqrt(num)

# Using math.ceil() to get the smallest integer greater than or equal to the number
ceiling = math.ceil(num)

# Using math.floor() to get the largest integer less than or equal to the number
floor_value = math.floor(num)

# Displaying the results
print("Square root:", square_root)
print("Ceiling value:", ceiling)
print("Floor value:", floor_value)

# Example of using the random module in Python

# Importing the random module
import random

# Generating a random integer between 1 and 100
rand_int = random.randint(1, 100)

# Generating a random floating-point number between 0 and 1
rand_float = random.random()

# Generating a random element from a list
sample_list = [10, 20, 30, 40, 50]
rand_choice = random.choice(sample_list)

# Displaying the results
print("Random integer between 1 and 100:", rand_int)
print("Random floating-point number between 0 and 1:", rand_float)
print("Random element from the list:", rand_choice)
