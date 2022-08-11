import unittest
from tree import Node

class CreateNode(unittest.TestCase):
    def test_single_node(self):
        tree = Node("root")
        self.assertEqual(tree.key,"root")

    def test_single_node_value(self):
        tree = Node("root", 10)
        self.assertEqual(tree.key,"root")
        self.assertEqual(tree.value,10)

    def test_traverse_node_shortcut(self):
        tree = Node("root")
        tree.try_new_leaf("shortcut")
        self.assertEqual(tree["shortcut"], tree._children["shortcut"])

    def test_add_new_leaf(self):
        tree = Node("root")
        tree.try_new_leaf("node 1")

        self.assertEqual(tree["node 1"].parent, tree,
            "The parent of the new leaf should be the creator node")
        self.assertEqual(tree["node 1"].key, "node 1")

    def test_add_new_leaf_value(self):
        tree = Node("root")
        tree.try_new_leaf("node 1", (2,"foo"))
        self.assertEqual(tree["node 1"].value, (2,"foo"))

    def test_remove_node(self):
        tree = Node("root")
        tree.try_new_leaf("node 1")
        tree.try_new_leaf("node 2")
        self.assertEqual(len(tree._children),2)

        del tree["node 1"]
        self.assertEqual(len(tree._children),1)

        del tree["node 2"]
        self.assertEqual(tree._children, {})

    def test_raise_if_children_modified(self):
        tree = Node("root")


if __name__ == "__main__":
     unittest.main()