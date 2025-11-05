class student:
    clg = "tops"
    def __init__(self):
        self.id = id 
        self.name = "name"
        self.email = "email"
    
    def display(self):
        print(self.id,self.name,self.email,self.clg)

    @classmethod
    def test(cls):
        print("test calling"+cls.clg)

    @staticmethod
    def run():
        print("run calling")

student.test()




