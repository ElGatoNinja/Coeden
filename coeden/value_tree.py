from __future__ import annotations
from coeden.specialClasses.base_node import Node



class ValueNode(Node):
    '''Repesents a node in a tree data structure, '''
    def __init__(self,key, value = None, parent = None):
        super().__init__(key,parent)
        self.value = value

    def __set_child(self, child: Node):
        if self._children is None:
            self._children = {}
        if child.key in self._children:
            raise ValueError(f'This node already has a child with key: "{child.key}".')

        child._parent = self
        self._children[child.key] = child

    def new_leaf(self, key, value = None):
        self.__set_child(ValueNode(key, value))

    def try_new_leaf(self,key, value=None):
        '''Create a node as a child of the caller node. If succesful returns true,
        if node already exist return false'''
        try:
            self.__set_child(ValueNode(key,value))
            return True
        except ValueError:
            return False

    def try_remove_leaf(self, key):
        '''Try to remove a leaf from the tree by key, if success returns True'''
        #not a leaf if it has children
        if self[key].children is True:
            return False
        try:
            self[key].parent = None
            del self._children[key]
            return True
        except:
            return False

    def print_tree(self):
        '''Print to console a graphical representation of the tree starting in the current node'''
        for (node, depth) in self.deep_first_iter():
            line = f'{(depth) * "   "}{node.key}'
            if node.value is not None:
                line += f' -> {node.value}'
            print(line)


                
