import unittest
from ..common.binary_tree import BinaryTree


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.perfect_bt = dict()
        self.perfect_bt['5'] = {'left': '3', 'right': '7'}
        self.perfect_bt['3'] = {'left': '2', 'right': '4'}
        self.perfect_bt['7'] = {'left': '6', 'right': '8'}

        self.unbalanced_bt = dict()
        self.unbalanced_bt['5'] = {'left': '3', 'right': '7'}
        self.unbalanced_bt['3'] = {'left': '2', 'right': '4'}
        self.unbalanced_bt['7'] = {'left': '6', 'right': '8'}
        self.unbalanced_bt['8'] = {'left': '1', 'right': '10'}
        self.unbalanced_bt['10'] = {'right': '0'}

    def test_perfect_bt(self):
        bt = BinaryTree(self.perfect_bt, '5')
        print(bt)
        self.assertTrue(bt.is_balanced())

    def test_unbalanced_bt(self):
        bt = BinaryTree(self.unbalanced_bt, '5')
        print(bt)
        self.assertFalse(bt.is_balanced())


if __name__ == '__main__':
    unittest.main()
