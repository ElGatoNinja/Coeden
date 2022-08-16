from collections import deque
import tree


class NoNode:
    '''works as a node, alows to traverse inexisting paths of the tree without errors'''
    def __init__(self, key, parent):
        self.key = None
        self.value = None
        self.parent = None

        self.__no_key = key
        self.__no_parent = parent

    def __eq__(self, other):
        return None is other

    def __getitem__(self,key):
        return NoNode(key,self)

    def create_all(self):
        last_real_node = self.__no_parent
        chain_keys = deque([self.__no_key])
        while isinstance(last_real_node, NoNode):
            chain_keys.appendleft(last_real_node.__no_key)
            last_real_node = last_real_node.__no_parent

        for key in chain_keys:
            last_real_node = tree.Node(key, parent=last_real_node)