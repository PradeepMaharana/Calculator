#!/usr/bin/env python3
"""Simple Calculator Application"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("=" * 40)
    print("       Simple Calculator")
    print("=" * 40)
    print("\nOperations:")
    print("  +  Addition")
    print("  -  Subtraction")
    print("  *  Multiplication")
    print("  /  Division")
    print("  q  Quit")
    print("\n" + "=" * 40)

    while True:
        try:
            # Get operation
            operation = input("\nEnter operation (+, -, *, /, q): ").strip().lower()

            if operation == 'q':
                print("Thank you for using the calculator!")
                break

            if operation not in ['+', '-', '*', '/']:
                print("Invalid operation. Please enter +, -, *, /, or q")
                continue

            # Get numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform calculation
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)

            # Display result
            print(f"\n{num1} {operation} {num2} = {result}")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()
