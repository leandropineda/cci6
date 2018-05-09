from .node import Node
from typing import Dict, List


class Graph(object):
    def __init__(self, adj_list: Dict[str, List[str]] = None):
        self.nodes: Dict[str, Node] = dict()

        if adj_list:
            self._populate(adj_list)

    def find(self, node: Node) -> Node:
        if not self.exists(node):
            return Node('')

    def exists(self, node: Node) -> bool:
        return node.name in self.nodes.keys()

    def get_node(self, node: Node) -> Node:
        return self.nodes.get(node.name)

    def _populate(self, adj_list: Dict[str, List[str]]):
        del self.nodes
        self.nodes = dict()
        for node_name, children in adj_list.items():
            n = Node(node_name)
            for child in children:
                n.insert_child(Node(child))
            self.nodes[node_name] = n


def tree_to_adj_list(graph: Graph) -> dict:
    adj_list = dict()
    nodes = graph.nodes.values()
    for node in nodes:
        node_children = node.get_children()
        adj_list[node.name] = [child.name for child in node_children]

    return adj_list


def path_exists(graph: Graph, node_a: Node, node_b: Node) -> bool:
    if node_a.name == node_b.name:
        return True
    node_graph_a = graph.get_node(node_a)
    node_graph_b = graph.get_node(node_b)
    exists = False
    for node in node_graph_a.get_children():
        if path_exists(graph, graph.get_node(node), node_graph_b):
            exists = True

    return exists
