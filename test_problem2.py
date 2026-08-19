import unittest
from pathlib import Path

from problem2_calculator import evaluate


class Problem2CalculatorTests(unittest.TestCase):
    def test_addition_and_subtraction(self):
        self.assertEqual(evaluate("3 + 5 - 2"), 6)

    def test_operator_precedence(self):
        self.assertEqual(evaluate("10 - 2 * 3"), 4)

    def test_parentheses_override_precedence(self):
        self.assertEqual(evaluate("(1 + 2) * 3"), 9)

    def test_nested_parentheses(self):
        self.assertEqual(evaluate("(2 + (3 - 1)) * 4"), 16)

    def test_division_and_decimal_result(self):
        self.assertEqual(evaluate("7 / 2"), 3.5)

    def test_ignores_spaces(self):
        self.assertEqual(evaluate(" 18 / ( 3 + 3 ) "), 3)

    def test_supports_negative_numbers(self):
        self.assertEqual(evaluate("-3 + (-2) * (-2)"), 1)

    def test_supports_negative_number_after_operator(self):
        self.assertEqual(evaluate("10 + -3"), 7)

    def test_rejects_mismatched_parentheses(self):
        with self.assertRaises(ValueError):
            evaluate("(1 + 2")

    def test_rejects_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate("10 / 0")

    def test_rejects_empty_expression(self):
        with self.assertRaises(ValueError):
            evaluate("   ")

    def test_original_expression_file(self):
        expressions = Path("Test 2 arithmetic expression/2_Expression.txt").read_text().splitlines()
        expected = [6, 9, 16, -4, 5, 41.5, 1, 75]
        for expression, expected_result in zip(expressions, expected):
            actual = evaluate(expression)
            print(f"โจทย์: {expression}\nผลลัพธ์: {actual}\n")
            self.assertEqual(actual, expected_result)


if __name__ == "__main__":
    unittest.main()
