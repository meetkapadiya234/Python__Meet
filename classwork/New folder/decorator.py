# def before(test):
#     def wapper(*a):
#         print(a[0]*a[0])
#         print("this is before decorator")
#         test(a)
#         return wapper
    
# @before
# def test(a):
#     print("this is a test function",a)


# test(10)


#  use decorator to calculate of a ,b 
# def decor(test):
#     def wapper(*a):
#         print("this is a decorator function")
#         test(a)
#         print("sum of a and b is :",a[0]+a[1])
#         print("multiplication of a and b is :",a[0]*a[1])
#         print("subtraction of a and b is :",a[0]-a[1])
#     return wapper
# @decor
# def test(a):
#     print("this is a test function",a)
# test(10,20)



def decor(test):
     def wapper(*a):
         print("this is a decorator function")
         test(a)
         print("sum of a and b is :",a[0]+a[1])
         print("multiplication of a and b is :",a[0]*a[1])
         print("subtraction of a and b is :",a[0]-a[1])
     return wapper

@decor
def test(a):
        print("this is a test function",a)
a = int(input("enter a : "))
b = int(input("enter b : "))
test(a,b)
