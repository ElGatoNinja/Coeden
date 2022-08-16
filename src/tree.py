from __future__ import annotations
from ast import match_case
from specialClasses import TreeIterator,WildNode,NoNode



class Node:
    '''Repesents a node in a tree data structure, '''
    def __init__(self,key, value = None, parent = None):
        RESERVED_KEYS = ["__*__","__**__","__<-__"]
        if key in RESERVED_KEYS:
            raise ValueError(f'The key "{key}" has an special function and it is reserved')

        self.key = key
        self.value = value
        self._parent : Node | None = None
        self.parent = parent
        self._children: dict = {}

    def __set_child(self, child: Node):
        if self._children is None:
            self._children = {}
        if child.key in self._children:
            raise ValueError(f'This node already has a child with key: "{child.key}".')

        child._parent = self
        self._children[child.key] = child
    
    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, parent: Node | None):
        if parent is None:
            #If parent is removed this node is also removed form the parent childs
            if self._parent is not None:
                del self._parent._children[self.key]
            self._parent = None
        else:
            parent.__set_child(self) #also sets self parent


    def try_new_leaf(self,key, value=None):
        '''Create a node as a child of the caller node. If succesful returns true,
        if node already exist return false'''
        try:
            self.__set_child(Node(key,value))
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

    def __getitem__(self, child_key) -> Node | NoNode | WildNode:
        match child_key:
            case "__*__":
                nodes = []
                for (_,node) in self._children.items():
                    nodes.append(node)
                return WildNode(nodes)
            case "__**__":
                pass
            case "__<-__":
                return self.parent
            case _:
                try:
                    return self._children[child_key]
                except KeyError:
                    return NoNode(child_key, self)
        
    
    def __delitem__(self, child_key):
        if child_key not in self._children:
            raise KeyError(f'Node "{self.key}" is not linked to a node named "{child_key}"')
        self._children[child_key]._parent = None
        del self._children[child_key]
    
    def deep_first_iter(self):
        '''Create an iterator with the deep-first search algorithm'''
        return TreeIterator(self)

    def breadth_first_iter(self):
        '''Create and iterator with the breadth-first search algorithm'''
        return TreeIterator(self,False)

    def print_tree(self):
        '''Print to console a graphical representation of the tree starting in the current node'''
        for (node, depth) in self.deep_first_iter():
            line = f'{(depth) * "   "}{node.key}'
            if node.value is not None:
                line += f' -> {node.value}'
            print(line)


                
