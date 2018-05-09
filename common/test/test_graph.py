import unittest
from cci.common.graph import Graph, Node, tree_to_adj_list, path_exists


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.adj_list = dict()
        self.adj_list['0'] = ['1', '2', '3']
        self.adj_list['1'] = []
        self.adj_list['2'] = ['4', '5']
        self.adj_list['3'] = []
        self.adj_list['4'] = []
        self.adj_list['5'] = ['10']
        self.adj_list['10'] = []

    def test_something(self):
        g = Graph(self.adj_list)
        self.assertDictEqual(tree_to_adj_list(g), self.adj_list)

    def test_path_exists(self):
        g = Graph(self.adj_list)
        node_a = g.get_node(Node('0'))
        node_b = g.get_node(Node('10'))
        self.assertTrue(path_exists(g, node_a, node_b))

    def test_path_does_not_exist(self):
        g = Graph(self.adj_list)
        node_a = g.get_node(Node('10'))
        node_b = g.get_node(Node('1'))
        self.assertFalse(path_exists(g, node_a, node_b))


if __name__ == '__main__':
    unittest.main()
