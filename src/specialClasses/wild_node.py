from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tree import Node

class WildNode:
    '''Works as "any node"'''
    def __init__(self,nodes: list[Node]):
        self.__nodes = nodes

    def __getitem__(self, name: str):
        if name == "__*__":
            next_level_nodes = []
            for node in self.__nodes:
                for sub_node in node.children:
                    next_level_nodes.append(sub_node)
            return WildNode(next_level_nodes)
        else:
            for node in self.__nodes():
                if node.name == name:
                    return node
            return None