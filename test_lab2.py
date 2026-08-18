import unittest

from problem1_balanced import is_balanced
from problem2_calculator import evaluate
from problem3_subsets import format_subset, generate_subsets


class Lab2Tests(unittest.TestCase):
    def test_balanced_parentheses(self):
        self.assertTrue(is_balanced("([{}])"))
        self.assertFalse(is_balanced("([)]"))
        self.assertFalse(is_balanced("("))
        self.assertFalse(is_balanced("1"))
        self.assertFalse(is_balanced(""))

    def test_arithmetic_expression(self):
        self.assertEqual(evaluate("(1 + 2) * 3"), 9)
        self.assertEqual(evaluate("10 - 2 * 3"), 4)
        self.assertEqual(evaluate("18 / (3 + 3)"), 3)

    def test_generate_all_subsets(self):
        self.assertEqual(
            generate_subsets([1, 2]),
            [[], [2], [1], [1, 2]],
        )
        self.assertEqual(generate_subsets([]), [[]])
        self.assertEqual(format_subset([]), "{}")
        self.assertEqual(format_subset([1, 2]), "{1, 2}")


if __name__ == "__main__":
    unittest.main()
