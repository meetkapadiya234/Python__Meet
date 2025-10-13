
#for loop
number = 123454321
temp = number
sum = 0
for i in range(len(str(number))):
    rem = number % 10
    sum = (sum*10) + rem
    number = number // 10    
    print(sum)
if temp == sum:
    print(temp, "is a palindrome number")
else:
    print(temp, "is not a palindrome number")
#while loop
number = 123454321
temp = number
sum = 0
while number != 0:
    rem = number % 10
    sum = (sum*10) + rem
    number = number // 10
    print(sum)
if temp == sum:
    print(temp, "is a palindrome number")
else:
    print(temp, "is not a palindrome number")
    