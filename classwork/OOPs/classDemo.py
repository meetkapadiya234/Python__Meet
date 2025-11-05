class pen:

    price = 20
    color = "black"
    company = "cello" 

    def to_write(self):
        print("somthings")
        print(self.color,self.company,self.price)

p = pen()
p.price=100
p.to_write()


p1 = pen()
p1.price = 200
p1.to_write()