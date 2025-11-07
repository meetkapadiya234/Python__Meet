length = 10 
a = 0
b = 1
print(a,b, end=' ')

for i in range(length):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
    # while loop
    
    a = 0
    b = 1
    print(a, b, end=' ')
    i = 0
    while i < 10:
        c = a + b
        print(c, end=' ')
        a = b
        b = c
        i += 1
       