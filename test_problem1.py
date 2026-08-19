import tempfile
import unittest
from pathlib import Path
import re

from problem1_balanced import is_balanced, is_balanced_file, is_balanced_source


class Problem1BalancedBracketsTests(unittest.TestCase):
    def test_accepts_empty_pair(self):
        self.assertTrue(is_balanced("()"))

    def test_accepts_nested_mixed_brackets(self):
        self.assertTrue(is_balanced("([{}])"))

    def test_accepts_multiple_pairs(self):
        self.assertTrue(is_balanced("()[]{}"))

    def test_rejects_wrong_order(self):
        self.assertFalse(is_balanced("([)]"))

    def test_rejects_unclosed_brackets(self):
        self.assertFalse(is_balanced("({["))

    def test_rejects_unopened_closing_bracket(self):
        self.assertFalse(is_balanced(")"))

    def test_rejects_non_bracket_input(self):
        self.assertFalse(is_balanced("abc"))
        self.assertFalse(is_balanced(""))

    def test_source_mode_ignores_comments_and_strings(self):
        source = '''
        # unmatched bracket in comment: [
        value = "unmatched bracket in string: {"
        return (value)
        '''
        self.assertTrue(is_balanced_source(source))

    def test_source_mode_detects_unbalanced_code(self):
        source = "def example():\n    print('missing closing parenthesis'\n"
        self.assertFalse(is_balanced_source(source))

    def test_file_mode_reads_python_source(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "example.py"
            path.write_text("# comment [\nvalue = '{'\nreturn (value)\n")
            self.assertTrue(is_balanced_file(path))

    def test_original_problem1_files(self):
        folder = Path("Test 1 parentheses")
        expected = {
            1: True,
            2: True,
            3: True,
            4: False,
            5: False,
            6: False,
            7: True,
            8: False,
            9: False,
            10: True,
        }
        paths = sorted(
            folder.glob("test*.py"),
            key=lambda path: int(re.search(r"\d+", path.stem).group()),
        )
        for path in paths:
            case_number = int(re.search(r"\d+", path.stem).group())
            actual = is_balanced_file(path)
            print(f"โจทย์: {path.name}\nผลลัพธ์: {actual}\n")
            self.assertEqual(actual, expected[case_number])


if __name__ == "__main__":
    unittest.main()
