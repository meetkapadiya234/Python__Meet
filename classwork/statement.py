#conditonal  : if , elif , else
#looping     : for , while
#control     : break , continue , pass


marks = 78
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B+")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")

# looping statement
for i in range(1,11):
    print(i)
i = 1
while i <= 10:
    print(i)
    i += 1
# control statement
for i in range(1,11):
    if i == 5:
        break
    print(i)
for i in range(1,11):
    if i == 5:
        continue
    print(i)
for i in range(1,11):
    if i == 5:
        pass
    print(i)

    # pass example
def fun():
    pass
fun()

choice='y'
while choice != 'n':
    marks= int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("A+")
elif marks >= 80 and marks <=90:
    print("A")
elif marks >= 70 and marks <=80:
    print("B+")
elif marks >= 60 and marks <=70:
    print("B")
elif marks >= 50 and marks <=60:
    print("C")
elif marks >= 40 and marks <=50:
    print("D")
elif marks >= 0 and marks <=40:
    print("F")
else:
    print("Invalid marks")
choice = input("Do you want to continue  ? yor n : ")
