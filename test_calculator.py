#!/usr/bin/env python3
"""Unit tests for the Calculator Application"""

import unittest
from calculator import add, subtract, multiply, divide, power, modulo, square_root, factorial, absolute_value, percentage

class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions"""

    # Addition tests
    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(10, -5), 5)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

    def test_add_floats(self):
        self.assertAlmostEqual(add(2.5, 3.2), 5.7)

    # Subtraction tests
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 3), 7)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-5, -3), -2)

    def test_subtract_mixed_numbers(self):
        self.assertEqual(subtract(5, -3), 8)

    def test_subtract_zero(self):
        self.assertEqual(subtract(5, 0), 5)

    def test_subtract_floats(self):
        self.assertAlmostEqual(subtract(10.5, 3.2), 7.3)

    # Multiplication tests
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-4, -5), 20)

    def test_multiply_mixed_numbers(self):
        self.assertEqual(multiply(4, -5), -20)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply(2.5, 4.0), 10.0)

    # Division tests
    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_mixed_numbers(self):
        self.assertEqual(divide(10, -2), -5)

    def test_divide_floats(self):
        self.assertAlmostEqual(divide(10.0, 4.0), 2.5)

    def test_divide_by_zero(self):
        result = divide(10, 0)
        self.assertEqual(result, "Error: Division by zero")

    def test_divide_zero_by_number(self):
        self.assertEqual(divide(0, 5), 0)

    def test_divide_resulting_in_float(self):
        self.assertAlmostEqual(divide(7, 2), 3.5)


class TestCalculatorEdgeCases(unittest.TestCase):
    """Test edge cases for calculator functions"""

    def test_large_numbers(self):
        self.assertEqual(add(1000000, 2000000), 3000000)

    def test_very_small_numbers(self):
        self.assertAlmostEqual(add(0.0001, 0.0002), 0.0003, places=5)

    def test_multiply_large_numbers(self):
        self.assertEqual(multiply(1000, 1000), 1000000)

    def test_division_precision(self):
        self.assertAlmostEqual(divide(1, 3), 0.3333333, places=5)


class TestPower(unittest.TestCase):
    """Test cases for power function"""

    def test_power_basic(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(power(2, -2), 0.25)

    def test_power_fractional_exponent(self):
        self.assertAlmostEqual(power(4, 0.5), 2.0)

    def test_power_negative_base(self):
        self.assertEqual(power(-2, 3), -8)

    def test_power_negative_base_even_exponent(self):
        self.assertEqual(power(-2, 2), 4)


class TestModulo(unittest.TestCase):
    """Test cases for modulo function"""

    def test_modulo_basic(self):
        self.assertEqual(modulo(10, 3), 1)

    def test_modulo_zero_remainder(self):
        self.assertEqual(modulo(10, 5), 0)

    def test_modulo_negative_dividend(self):
        self.assertEqual(modulo(-10, 3), 2)

    def test_modulo_negative_divisor(self):
        self.assertEqual(modulo(10, -3), -2)

    def test_modulo_by_zero(self):
        result = modulo(10, 0)
        self.assertEqual(result, "Error: Modulo by zero")

    def test_modulo_floats(self):
        self.assertAlmostEqual(modulo(10.5, 3), 1.5)


class TestSquareRoot(unittest.TestCase):
    """Test cases for square root function"""

    def test_square_root_basic(self):
        self.assertEqual(square_root(9), 3)

    def test_square_root_perfect_square(self):
        self.assertEqual(square_root(16), 4)

    def test_square_root_zero(self):
        self.assertEqual(square_root(0), 0)

    def test_square_root_decimal(self):
        self.assertAlmostEqual(square_root(2), 1.414213, places=5)

    def test_square_root_negative(self):
        result = square_root(-4)
        self.assertEqual(result, "Error: Cannot calculate square root of negative number")

    def test_square_root_float(self):
        self.assertAlmostEqual(square_root(6.25), 2.5)


class TestFactorial(unittest.TestCase):
    """Test cases for factorial function"""

    def test_factorial_basic(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_small_number(self):
        self.assertEqual(factorial(3), 6)

    def test_factorial_negative(self):
        result = factorial(-5)
        self.assertEqual(result, "Error: Factorial of negative number is undefined")

    def test_factorial_large_number(self):
        self.assertEqual(factorial(10), 3628800)


class TestAbsoluteValue(unittest.TestCase):
    """Test cases for absolute value function"""

    def test_absolute_positive(self):
        self.assertEqual(absolute_value(5), 5)

    def test_absolute_negative(self):
        self.assertEqual(absolute_value(-5), 5)

    def test_absolute_zero(self):
        self.assertEqual(absolute_value(0), 0)

    def test_absolute_float(self):
        self.assertEqual(absolute_value(-3.14), 3.14)

    def test_absolute_negative_float(self):
        self.assertAlmostEqual(absolute_value(-2.5), 2.5)


class TestPercentage(unittest.TestCase):
    """Test cases for percentage function"""

    def test_percentage_basic(self):
        self.assertEqual(percentage(10, 100), 10)

    def test_percentage_fifty_percent(self):
        self.assertEqual(percentage(50, 200), 100)

    def test_percentage_decimal(self):
        self.assertAlmostEqual(percentage(15, 300), 45)

    def test_percentage_small_percentage(self):
        self.assertAlmostEqual(percentage(1, 500), 5)

    def test_percentage_zero(self):
        self.assertEqual(percentage(0, 100), 0)

    def test_percentage_negative(self):
        self.assertEqual(percentage(-10, 100), -10)


if __name__ == "__main__":
    unittest.main()
