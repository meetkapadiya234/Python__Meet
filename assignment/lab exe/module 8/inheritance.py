# single inheritance example in Python

# Parent class
class Parent:
    def greet(self):
        print("Hello from Parent")

# Child class
class Child(Parent):
    def welcome(self):
        print("Welcome from Child")

# Using the child class
c = Child()
c.greet()    # inherited from Parent
c.welcome()  # own method

# multiple inheritance example in Python

# Parent classes
class Parent1:
    def greet1(self):
        print("Hello from Parent1")

class Parent2:
    def greet2(self):
        print("Hello from Parent2")

# Child class inheriting from both parents
class Child(Parent1, Parent2):
    def welcome(self):
        print("Welcome from Child")

c = Child()
c.greet1()   # from Parent1
c.greet2()   # from Parent2
c.welcome()  # own method


# multilevel inheritance example in Python

# Grandparent class
class Grandparent:
    def greet_gp(self):
        print("Hello from Grandparent")

# Parent class
class Parent(Grandparent):
    def greet_p(self):
        print("Hello from Parent")

# Child class
class Child(Parent):
    def greet_c(self):
        print("Hello from Child")

c = Child()
c.greet_gp()  # inherited from Grandparent
c.greet_p()   # inherited from Parent
c.greet_c()   # own method

# hierarchical inheritance example in Python

# Parent class
class Parent:
    def greet(self):
        print("Hello from Parent")

# Multiple child classes
class Child1(Parent):
    def greet1(self):
        print("Hello from Child1")

class Child2(Parent):
    def greet2(self):
        print("Hello from Child2")

c1 = Child1()
c2 = Child2()
c1.greet()   # inherited from Parent
c2.greet()   # inherited from Parent

# hybrid inheritance example in Python

# Combination of multiple and multilevel inheritance

class A:
    def greet_a(self):
        print("Hello from A")

class B(A):
    def greet_b(self):
        print("Hello from B")

class C(A):
    def greet_c(self):
        print("Hello from C")

class D(B, C):
    def greet_d(self):
        print("Hello from D")

d = D()
d.greet_a()  # inherited via B/C
d.greet_b()
d.greet_c()
d.greet_d()
