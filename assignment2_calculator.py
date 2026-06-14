# Simple Calculator

print("===== SIMPLE CALCULATOR =====")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, //, %, **): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    result = num1 / num2

elif operator == "//":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    result = num1 // num2

elif operator == "%":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    result = num1 % num2

elif operator == "**":
    result = num1 ** num2

else:
    print("Invalid operator.")
    exit()

if operator == "/":
    print(f"\nResult: {num1} {operator} {num2} = {result:.4f}")
else:
    print(f"\nResult: {num1} {operator} {num2} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is zero.")

print("==============================")