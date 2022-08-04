class NoNode:
    '''works as a node, alows to traverse inexisting paths of the tree without errors'''
    def __eq__(self, other):
        return None
    def __getitem__(self,name):
        return NoNode()