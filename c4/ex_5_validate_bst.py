import unittest
from ..common.binary_tree import BinaryTree


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.bst = dict()
        self.bst['5'] = {'left': '3', 'right': '7'}
        self.bst['3'] = {'left': '2', 'right': '4'}
        self.bst['7'] = {'left': '6', 'right': '8'}

        self.no_bst = dict()
        self.no_bst['5'] = {'left': '3', 'right': '7'}
        self.no_bst['3'] = {'left': '2', 'right': '10'}
        self.no_bst['7'] = {'left': '6', 'right': '8'}

    def test_tree_is_bst(self):
        bt = BinaryTree(self.bst, '5')
        print(bt)
        self.assertTrue(bt.is_bst(), True)
        bt_no_bst = BinaryTree(self.no_bst, '5')
        print(bt_no_bst)
        self.assertFalse(bt_no_bst.is_bst(), False)


if __name__ == '__main__':
    unittest.main()
