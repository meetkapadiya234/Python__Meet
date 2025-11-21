# Example of exception handling in Python

# Simple calculator with exception handling

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", num1 / num2)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter a valid number.")

finally:
    print("Execution completed.")   

# /// example of handling multiple exceptions

    # Handling multiple exceptions

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter a valid integer.")

except Exception as e:
    print("An unexpected error occurred:", e)
