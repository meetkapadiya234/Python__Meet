class Animal:

    def __init__(self,name):
        self.name = name

    def voice(self):
        print("generice animal voice")

class Dog(Animal):

    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    
    def display(self):
        print(self.name.self.breed,self.a)

    def voice(self):
        print("Woof Woof")

class Cat(Animal):

    def __init__(self,name,color):
        super().__init__(name)
        self.color = color
    def display(self):
        print(self.name,self.breed,)

    def voice(self):
        print("meow...meow")

d = Dog("tommy","labrodar")
d.display()
d.voice()

c = Cat("pushpa","white")
c.display()
c.voice()