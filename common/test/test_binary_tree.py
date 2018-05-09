import unittest
from ..binary_tree import BinaryTree

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

    def test_tree_height(self):
        bbt = BinaryTree(self.perfect_bt, '5')
        self.assertEqual(bbt.tree_height(), 2)
        ubt = BinaryTree(self.unbalanced_bt, '5')
        self.assertEqual(ubt.tree_height(), 4)


if __name__ == '__main__':
    unittest.main()
