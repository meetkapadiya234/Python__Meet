number = 100 to 999
temp = number
sum = 0
while number!=0:
    rem = number % 10
    sum = sum + (rem**3)
    number = number//10
    
    if temp==sum:
        print(temp, "is an Armstrong number")  
    else:
     print(temp, "is not an Armstrong number")

