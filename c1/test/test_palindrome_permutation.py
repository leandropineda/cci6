"""
INPUT   Tact Coa
Output  True (permutations: "taco cat", "atco cta", etc)
"""

import unittest

from cci.c1.palindrome_permutation import is_permutation_palindrome

class MyTestCase(unittest.TestCase):
    def test_something(self):
        _input = "Tact Coa"
        self.assertEqual(is_permutation_palindrome(_input), True)


if __name__ == '__main__':
    unittest.main()
