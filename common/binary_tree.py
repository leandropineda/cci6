from .node import BinaryNode
from typing import Dict


class BinaryTree(object):
    def __init__(self, adj_list: Dict[str, Dict[str, str]], root: str):
        self.nodes: Dict[str, BinaryNode] = dict()
        self._populate(adj_list)
        self.root: str = root

    def __str__(self):
        bn_root = self._get_root_node()
        return self._to_str(bn_root)

    def _to_str(self, node: BinaryNode) -> str:
        if not node.is_leaf():
            return "(" + str(node) + ",(" + str(self._to_str(self.get_node(node.left))) + "," + str(self._to_str(self.get_node(node.right))) + "))"
        return "(" + str(node.name) + ")"

    def _get_root_node(self) -> BinaryNode:
        return self.get_node(self.root)

    def _populate(self, adj_list: Dict[str, Dict[str, str]]):
        for node_name, children in adj_list.items():
            bn = self.nodes.get(node_name, BinaryNode(node_name))
            bn.left = children.get('left')
            bn.right = children.get('right')
            bn.successor = children.get('successor')
            self.nodes[node_name] = bn

    def is_balanced(self) -> bool:
        bt_root = self.nodes.get(self.root)
        return abs(self._tree_height(bt_root.left) - self._tree_height(bt_root.right)) <= 1

    def get_node(self, node_name) -> BinaryNode:
        if node_name not in self.nodes.keys():
            return BinaryNode(node_name)
        return self.nodes[node_name]

    def _tree_height(self, node: str) -> int:
        bt_node = self.nodes.get(node)
        if bt_node is None:
            return 0

        return max([self._tree_height(bt_node.left), self._tree_height(bt_node.right)]) + 1

    def tree_height(self) -> int:
        return self._tree_height(self.root)

    def is_bst(self) -> bool:
        return self._is_bst(self._get_root_node())

    def _max(self, node: BinaryNode) -> int:
        if node.is_leaf():
            return int(node.name)
        return max([int(self.get_node(node.left).name), int(self.get_node(node.right).name)])

    def _is_bst(self, node: BinaryNode) -> bool:
        if node.is_leaf():
            return True
        return self._max(self.get_node(node.left)) < int(node.name) and \
               self._max(self.get_node(node.right)) > int(node.name)