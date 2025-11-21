# Example of defining a class and creating objects in Python

# Defining a class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object of the class
student1 = Student("Alice", 20)

# Accessing properties using the object
print("Name:", student1.name)
print("Age:", student1.age)
