class Demo:

    def __init__(self,a,b):
         self.a = a
         self.b = b
    
    def display(self):
         print("hello")

    def __str__(self):
         return f"Demo with a: {self.a} and b: {self.b}"

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Demo with value: {self.value}"

    def __eq__(self, other):
            return self.value == other.value
    
d1 = Demo(10,20)
d2 = Demo(10,30)
print(d1)  # This will call the __str__ method
print(d1 == d2)  # This will call the __eq__ method

