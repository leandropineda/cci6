"""
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""

import unittest

from cci.c1.string_edits import string_edits


class MyTestCase(unittest.TestCase):
    def test_string_removal(self):
        _string1 = "pale"
        _string2 = "ple"
        self.assertTrue(string_edits(_string1, _string2))

    def test_string_addition(self):
        _string1 = "pales"
        _string2 = "pale"
        self.assertTrue(string_edits(_string1, _string2))

    def test_string_replace(self):
        _string1 = "pale"
        _string2 = "bale"
        self.assertTrue(string_edits(_string1, _string2))

    def test_string_false(self):
        _string1 = "pale"
        _string2 = "bake"
        self.assertFalse(string_edits(_string1, _string2))


if __name__ == '__main__':
    unittest.main()
