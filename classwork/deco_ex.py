
def show(*a):
    print("Both checks passed:", a)

def onlyCapital():
    def decor(test):
        def wapper(*a):
            if all(i.isupper() for i in a):
                test(a)
            else:
                print("all letters must be capital")
        return wapper
    return decor
@onlyCapital()
def show(*a):
    print("Both checks passed:", a) 
show("MEET ")


def onlychar():
    def decor(test):
        def wapper(*a):
            if all(i.isalpha() for i in a):
                test(a)
            else:
                print("only characters are allowed")
        return wapper
    return decor
@onlychar()


def show(*a):
        print("Both checks passed:", a)
show("Meet")

def onlynumber():
    def decor(test):
        def wapper(*a):
            if all(i.isdigit() for i in a):
                test(a)
            else:
                print("only numbers are allowed")
        return wapper
    return decor
@onlynumber()
def show(*a):
        print("Both checks passed:", a)

show("123")
    