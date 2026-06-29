#!/usr/bin/env python3
"""Unit tests for the Calculator Application"""

import unittest
from calculator import add, subtract, multiply, divide

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


if __name__ == "__main__":
    unittest.main()
