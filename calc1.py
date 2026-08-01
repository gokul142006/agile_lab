# Get input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithmetic operations
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

# Check before division
if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")