num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")

sum_num = num1 + num2
print("Sum =", sum_num)

if sum_num < 2:
    print("The sum is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(sum_num ** 0.5) + 1):
        if sum_num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("The sum is a prime number.")
    else:
        print("The sum is not a prime number.")

temp = str(sum_num)

if temp == temp[::-1]:
    print("The sum is a palindrome.")
else:
    print("The sum is not a palindrome.") 