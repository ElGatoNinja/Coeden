from __future__ import annotations
from collections import deque
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from base_node import Node


class TreeIterator:
    '''Alow to iterate a tree with both deep first and breadth first search algorithms'''
    def __init__(self,root_node: Node, deep_first=True):
        self.queue = deque()
        self.queue.append((root_node,0))
        self.deep_first = deep_first

    def _pop_next_node(self):
        if self.deep_first:
            return self.queue.pop()
        else:
            return self.queue.popleft()
    
    def __iter__(self):
        return self

    def __next__(self):
        if not self.queue:
            raise StopIteration

        (node, depth) = self._pop_next_node()
        if node.children:
            for _,child in node.children.items():
                self.queue.append((child, depth + 1))
        return (node,depth)
