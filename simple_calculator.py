# Simple Calculator

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get the operator
operator = input("Enter an operator (+, -, *, /): ")

# Perform the calculation
if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    print("Result:", num1 / num2)

else:
    print("Invalid operator")
