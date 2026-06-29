#!/usr/bin/env python3
"""Simple Calculator Application"""

import math

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

def power(x, y):
    return x ** y

def modulo(x, y):
    if y == 0:
        return "Error: Modulo by zero"
    return x % y

def square_root(x):
    if x < 0:
        return "Error: Cannot calculate square root of negative number"
    return math.sqrt(x)

def factorial(n):
    if n < 0:
        return "Error: Factorial of negative number is undefined"
    if not isinstance(n, int) or n != int(n):
        return "Error: Factorial requires a non-negative integer"
    return math.factorial(int(n))

def absolute_value(x):
    return abs(x)

def percentage(x, y):
    return (x / 100) * y

def calculator():
    print("=" * 50)
    print("         Advanced Calculator")
    print("=" * 50)
    print("\nBasic Operations:")
    print("  +   Addition")
    print("  -   Subtraction")
    print("  *   Multiplication")
    print("  /   Division")
    print("\nAdvanced Operations:")
    print("  ^   Power (exponentiation)")
    print("  %   Modulo (remainder)")
    print("  sqrt Square root (single number)")
    print("  !   Factorial (single number)")
    print("  abs Absolute value (single number)")
    print("  pct Percentage (x% of y)")
    print("\nOther:")
    print("  q   Quit")
    print("=" * 50)

    while True:
        try:
            # Get operation
            operation = input("\nEnter operation (+, -, *, /, ^, %, sqrt, !, abs, pct, q): ").strip().lower()

            if operation == 'q':
                print("Thank you for using the calculator!")
                break

            # Single number operations
            if operation in ['sqrt', '!', 'abs']:
                num = float(input("Enter number: "))

                if operation == 'sqrt':
                    result = square_root(num)
                elif operation == '!':
                    result = factorial(num)
                elif operation == 'abs':
                    result = absolute_value(num)

                print(f"\n{operation}({num}) = {result}")

            # Two number operations
            elif operation in ['+', '-', '*', '/', '^', '%', 'pct']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if operation == '+':
                    result = add(num1, num2)
                    display_op = '+'
                elif operation == '-':
                    result = subtract(num1, num2)
                    display_op = '-'
                elif operation == '*':
                    result = multiply(num1, num2)
                    display_op = '*'
                elif operation == '/':
                    result = divide(num1, num2)
                    display_op = '/'
                elif operation == '^':
                    result = power(num1, num2)
                    display_op = '^'
                elif operation == '%':
                    result = modulo(num1, num2)
                    display_op = '%'
                elif operation == 'pct':
                    result = percentage(num1, num2)
                    display_op = '% of'

                print(f"\n{num1} {display_op} {num2} = {result}")

            else:
                print("Invalid operation. Please enter a valid operation.")
                continue

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()
