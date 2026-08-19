import unittest
from pathlib import Path

from problem3_subsets import _read_items, format_subset, generate_subsets


class Problem3SubsetsTests(unittest.TestCase):
    def test_generates_empty_subset_for_empty_input(self):
        self.assertEqual(generate_subsets([]), [[]])

    def test_generates_all_subsets_in_expected_order(self):
        self.assertEqual(
            generate_subsets([1, 2]),
            [[], [2], [1], [1, 2]],
        )

    def test_generates_two_to_the_n_subsets(self):
        subsets = generate_subsets([1, 2, 3])
        self.assertEqual(len(subsets), 8)
        self.assertEqual(
            {tuple(subset) for subset in subsets},
            {
                (),
                (1,),
                (2,),
                (3,),
                (1, 2),
                (1, 3),
                (2, 3),
                (1, 2, 3),
            },
        )

    def test_does_not_modify_original_input(self):
        items = [1, 2, 3]
        generate_subsets(items)
        self.assertEqual(items, [1, 2, 3])

    def test_formats_empty_and_non_empty_subsets(self):
        self.assertEqual(format_subset([]), "{}")
        self.assertEqual(format_subset([1, 2]), "{1, 2}")

    def test_reads_nested_set_members_without_splitting_inner_commas(self):
        self.assertEqual(_read_items("{{1},{2},{3}}"), ["{1}", "{2}", "{3}"])

    def test_original_set_file(self):
        lines = Path("Test 3 possible subsets/SetT.txt").read_text().splitlines()
        parsed = [_read_items(line) for line in lines]
        expected = [[], [1], [1, 2], [1, 2, 3], ["{1}", "{2}", "{3}"]]
        for problem, actual, expected_result in zip(lines, parsed, expected):
            result = generate_subsets(actual)
            print(f"โจทย์: {problem}\nผลลัพธ์: {[format_subset(subset) for subset in result]}\n")
            self.assertEqual(actual, expected_result)


if __name__ == "__main__":
    unittest.main()
