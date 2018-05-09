import unittest
from ..common.sort import merge_sort


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.unsorted_arr = [1, 6, 2, 9, 5]
        self.sorted_arr = [1, 2, 5, 6, 9]

    def test_merge_sort_one_element(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_merge_sort_empty_arr(self):
        self.assertEqual(merge_sort([]), [])

    def test_merge_sort(self):
        self.assertEqual(self.sorted_arr, merge_sort(self.unsorted_arr))


if __name__ == '__main__':
    unittest.main()
