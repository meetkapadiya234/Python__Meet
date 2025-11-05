class A:
    def display(self):
        print("A display calling")

class B:
    def display(slf):
        print("B display calling")

class C(A,B):
    def display(self):
        print("C display calling")

c = C()
c.display()
