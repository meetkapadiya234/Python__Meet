l = [15,54,45,78,96,32,14,65,89,23]
k = iter(l)

print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))  
print(next(k))
print(next(k))
print(next(k))
print(next(k))

#  generator function
def sqaure(a):
    for i in range(a):
        yield i*i
k = iter (sqaure(10))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))