import unittest
from tree import Node

class CreateNode(unittest.TestCase):
    def test_single_node(self):
        root = Node("root")
        self.assertEqual(root.name,"root")

if __name__ == "__main__":
     unittest.main()