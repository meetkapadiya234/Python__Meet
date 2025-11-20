# 1. Comments
# This is a simple Python program to greet a user

# 2. Import (optional, if needed)
import datetime

# 3. Variables
name = "Meet"
age = 20

# 4. Function
def greet(user_name, user_age):

    print("Hello,", user_name)
    print("You are", user_age, "years old.")
    print("Current year is:", datetime.datetime.now().year)

# 5. Main program (execution starts here)

greet(name, age)

# 6. input fuction to take user input (optional)
name = input("Enter your name: ")
print("Hello,", name)

# 7. type fuction to check data type (optional)
x = 10
print(type(x))
