import unittest
from tree import ValueNode

class CreateNode(unittest.TestCase):
    def test_single_node_value(self):
        tree = ValueNode("root", 10)
        self.assertEqual(tree.key,"root")
        self.assertEqual(tree.value,10)

    def test_add_new_leaf_value(self):
        tree = ValueNode("root")
        tree.try_new_leaf("node 1", (2,"foo"))
        self.assertEqual(tree["node 1"].value, (2,"foo"))

if __name__ == "__main__":
    unittest.main()