from specialClasses import TreeIterator,WildNode,NoNode

class Node:
    '''Repesents a node in a tree data structure, '''
    def __init__(self,name: str, value = None, parent = None):
        self.name = name
        self.value = value
        self.__parent = None
        self._set_parent(parent)
        self.children = None

    def _get_parent(self):
        return self.__parent
    
    def _set_parent(self, parent):
        if parent is not None:
            self.__parent = parent
            if self.__parent.children is None:
                self.__parent.children = {}
            self.__parent.children[self.name] = self
        else:
            #If parent is removed this node is also removed form the parent childs
            if self.__parent is not None:
                del self.__parent.children[self.name]
            self.__parent = None

    parent = property(_get_parent, _set_parent)

    def new_leaf(self,name: str, value=None):
        '''Create a node as a child of the caller node. If succesful returns true, if node already exist return false'''
        if not self.children:
            self.children = {}
        if name in self.children:
            return False

        self.children[name] = Node(name,value)
        self.children[name].parent = self
        return True

    def try_remove_leaf(self, name):
        '''Try to remove a leaf from the tree by name, if success returns True'''
        #not a leaf if it has children
        if self[name].children is True:
            return False
        try:
            self[name].parent = None
            del self.children[name]
            return True
        except:
            return False

    def __getitem__(self, child_name: str):
        if child_name == "__*__":
            nodes = []
            for (_,node) in self.children.items():
                nodes.append(node)
            return WildNode(nodes)

        try:
            return self.children[child_name]
        except KeyError:
            return None
    
    def deep_first_iter(self):
        '''Create an iterator with the deep-first search algorithm'''
        return TreeIterator(self)

    def breadth_first_iter(self):
        '''Create and iterator with the breadth-first search algorithm'''
        return TreeIterator(self,False)

    def print_tree(self):
        '''Print to console a graphical representation of the tree starting in the current node'''
        for (node, depth) in self.deep_first_iter():
            line = f'{(depth) * "   "}{node.name}'
            if node.value is not None:
                line += f' -> {node.value}'
            print(line)

                
