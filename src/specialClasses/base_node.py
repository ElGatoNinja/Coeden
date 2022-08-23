from __future__ import annotations
import abc
from collections import deque
from src.specialClasses.tree_iterator import TreeIterator

class NodeTraverse(abc.ABC):
    @abc.abstractclassmethod
    def __getitem__(self, key) -> NodeTraverse:
        pass

    def _match_special_keys(self,node,key):
        match key:
            case "__*__":
                nodes = list(node._children.values())
                return NodeSet(nodes)
            case "__**__":
                pass
                #iterate tree
            case "__<-__":
                return node._parent
            case _:
                return None

class Node(NodeTraverse):
    def __init__(self, key, parent = None):
        RESERVED_KEYS = ["__*__","__**__","__<-__"]
        if key in RESERVED_KEYS:
            raise ValueError(f'The key "{key}" has an special function and it is reserved')

        self.key = key
        self._parent : Node | None = None
        self.parent = parent
        self._children: dict = {}

    def __set_child(self, child: Node):
        if self._children is None:
            self._children = {}
        if child.key in self._children:
            raise KeyError(f'This node already has a child with key: "{child.key}".')

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

    def __getitem__(self, child_key) -> NodeTraverse:
        special = self._match_special_keys(self,child_key)
        if special is not None:
            return special

        try:
            return self._children[child_key]
        except KeyError:
            return NoNode(child_key, self)

    def __delitem__(self, child_key):
        if child_key not in self._children:
            raise KeyError(f'Node "{self.key}" is not linked to a node named "{child_key}"')
        self._children[child_key]._parent = None
        del self._children[child_key]
    
    def new_leaf(self, key):
        '''Create a node as a child of the caller node'''
        self.__set_child(Node(key))

    def try_new_leaf(self,key):
        '''Create a node as a child of the caller node. If succesful returns true,
        if node already exist return false'''
        try:
            self.__set_child(Node(key))
            return True
        except KeyError:
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
    
    def deep_first_iter(self):
        '''Create an iterator with the deep-first search algorithm'''
        return TreeIterator(self)

    def breadth_first_iter(self):
        '''Create and iterator with the breadth-first search algorithm'''
        return TreeIterator(self,False)


class NodeSet(NodeTraverse):
    '''Works as "any node"'''
    def __init__(self,nodes: list[Node]):
        self.__nodes = nodes

    def _node_set_special_keys(self,key):
        match key:
            case "__?__":
                if len(self.__nodes) > 0:
                    return self.__nodes[0]
                else:
                    #when there are special keys nonodes can not be created in chain, 
                    #so parent does not realy matter
                    return NoNode("__?__", parent=None)
            case _:
                return None


    def __getitem__(self, key) -> NodeTraverse:
        ns_special = self._node_set_special_keys(key)
        if ns_special is not None:
            return ns_special
        
        next_level_nodes = []
        for node in self.__nodes:   
            special = self._match_special_keys(node,key)
            if special is not None:
                if isinstance(special,list):
                    next_level_nodes += special
                else:
                    next_level_nodes.append(special)
            #try to acces by child keys
            elif node[key] != None:
                next_level_nodes.append(node[key])
        return NodeSet(next_level_nodes)

    def tolist(self):
        return self.__nodes

    def __iter__(self):
        self.__iter_index = 0

    def __next__(self):
        node = self.__nodes[self.__iter_index]
        self.__iter_index += 1
        return node


class NoNode(NodeTraverse):
    '''works as a node, alows to traverse inexisting paths of the tree without errors'''
    def __init__(self, key, parent):
        self.key = None
        self.value = None
        self.parent = None

        self.__no_key = key
        self.__no_parent = parent

    def __eq__(self, other):
        return None is other
    def __ne__(self, other):
        return None is not other

    def __getitem__(self,key) -> NoNode:
        return NoNode(key,self)

    def create_all(self):
        last_real_node = self.__no_parent
        chain_keys = deque([self.__no_key])
        while isinstance(last_real_node, NoNode):
            chain_keys.appendleft(last_real_node.__no_key)
            last_real_node = last_real_node.__no_parent

        for key in chain_keys:
            last_real_node = Node(key, parent=last_real_node)