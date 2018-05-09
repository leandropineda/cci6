"""
INPUT   "Mr John Smith     ", 13
OUTPUT  "Mr%20John%20Smith"
"""

import unittest

from cci.c1.urlify import urlify


class MyTestCase(unittest.TestCase):
    def test_urlify(self):
        _input = ("Mr John Smith     ", 13)
        _output = "Mr%20John%20Smith"
        self.assertEqual(urlify(_input[0], _input[1]), _output)


if __name__ == '__main__':
    unittest.main()
