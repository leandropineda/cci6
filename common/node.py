from typing import List, TypeVar

T = TypeVar('Node')


class Node(object):
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.children: List[T] = list()

    def get_children(self) -> List[T]:
        return self.children

    def insert_child(self, child: T) -> None:
        self.children.append(child)


class BinaryNode(object):
    def __init__(self, name: str, successor: str = None):
        self.name: str = name
        self.left: str = None
        self.right: str = None
        self.successor: str = successor

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    def __str__(self):
        return "(" + self.name + ")"

