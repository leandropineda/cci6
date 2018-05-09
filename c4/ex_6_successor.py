import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.bst = dict()
        self.bst['5'] = {'left': '3', 'right': '7'}
        self.bst['3'] = {'left': '2', 'right': '4'}
        self.bst['7'] = {'left': '6', 'right': '8'}


if __name__ == '__main__':
    unittest.main()
