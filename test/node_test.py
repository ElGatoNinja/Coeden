import unittest
from src import Node

class CreateNodes(unittest.TestCase):
    def test_single_node(self):
        tree = Node("root")
        self.assertEqual(tree.key,"root") 

    def test_add_new_leaf(self):
        tree = Node("root")
        tree.new_leaf("node 1")
        self.assertEqual(tree["node 1"].parent, tree,
            "The parent of the new leaf should be the creator node")
        self.assertEqual(tree["node 1"].key, "node 1")

    def test_remove_node(self):
        tree = Node("root")
        tree.new_leaf("node 1")
        tree.new_leaf("node 2")
        self.assertEqual(len(tree._children),2)

        del tree["node 1"]
        self.assertEqual(len(tree._children),1)

        del tree["node 2"]
        self.assertEqual(tree._children, {})    

    def test_try_new_leaf(self):
        tree = Node("root")
        first = tree.try_new_leaf("node 1")
        second = tree.try_new_leaf("node 1")

        self.assertEqual(first, True)
        self.assertEqual(second, False)

        self.assertNotEqual(tree["node 1"],None)