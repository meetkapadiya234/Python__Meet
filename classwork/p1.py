for i in range(0,6):
    for j in range(0,i):
        print("* ",end=" ")
    print("\n",end=" ")

#pattern 2
for i in range(5):
    print(" "*(5-i),"* "*(i+1))

#pattern 3
for i in range(5):
    print(" "*(5-i),"*"*(2*i+1))

#pattern 4
for i in range(5):
    print(" "*(5-i),"*"*(2*i+1))
for i in range(5,-1,-1):
    print(" "*(5-i),"*"*(2*i+1))

#pattern 5
n = 4  
for i in range(1, n+1):
    print(" "*(n-i) + "*" + " "*(2*(i-1)) + ("*" if i > 1 else " "))

for i in range(n-1, 0, -1):
    print(" "*(n-i) + "*" + " "*(2*(i-1)) + ("*" if i > 1 else " "))
