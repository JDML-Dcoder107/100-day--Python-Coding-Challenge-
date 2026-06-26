print(" Calculator ".center(22, "="))

allowed_operations = ['+', '-', '*', '/', '//']
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /, //): ")

    if operation not in allowed_operations:
        raise ValueError("Invalid operation. Please use one of the following: +, -, *, /, //.")

    result = eval(f"{num1} {operation} {num2}")
except ZeroDivisionError as e:
    result = "Error: Division by zero is not allowed."
except ValueError as e:
    result = "Error: Invalid input."

print(f"The result is: {result}")