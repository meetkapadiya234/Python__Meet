# Example of method overloading and overriding in Python

class Calculator:
    # Method with default arguments for overloading behavior
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()

print("Add two numbers:", calc.add(10, 20))
print("Add three numbers:", calc.add(10, 20, 30))

# example of method overriding

# Parent class
class Parent:
    def greet(self):
        print("Hello from Parent")

# Child class
class Child(Parent):
    def greet(self):
        print("Hello from Child")

c = Child()
c.greet()  # Calls the overridden method in Child
p = Parent()
p.greet()  # Calls the method in Parent

