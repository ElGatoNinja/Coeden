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

    def test_try_add_new_leaf(self):
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

class TraverseTree(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = Node("root")
        self.tree.try_new_leaf("fruits")
        self.tree["fruits"].try_new_leaf("red")
        self.tree["fruits"].try_new_leaf("yellow")
        self.tree["fruits"].try_new_leaf("purple")
        self.tree["fruits"].try_new_leaf("green")
        
        self.tree["fruits"]["red"].try_new_leaf("apple")
        self.tree["fruits"]["red"].try_new_leaf("strawberry")

        self.tree["fruits"]["yellow"].try_new_leaf("banana")
        self.tree["fruits"]["yellow"].try_new_leaf("pineapple")
        
        self.tree["fruits"]["purple"].try_new_leaf("berry")

        self.tree["fruits"]["green"].try_new_leaf("pear")
        self.tree["fruits"]["green"].try_new_leaf("apple")

        self.tree.try_new_leaf("tech companies")
        self.tree["tech companies"].try_new_leaf("apple", 345)
        self.tree["tech companies"].try_new_leaf("microsoft", 243)
        self.tree["tech companies"].try_new_leaf("google",348)
        self.tree["tech companies"].try_new_leaf("meta",145)


    def test_traverse_node_shortcut(self):
        self.tree.try_new_leaf("shortcut")
        self.assertEqual(self.tree["shortcut"], self.tree._children["shortcut"])

    def test_traverse_multiple_nodes(self):
        google = self.tree["tech companies"]["google"]
        self.assertEqual(google.key, "google")
        self.assertEqual(google.value,348)

        banana = self.tree["fruits"]["yellow"]["banana"]
        self.assertEqual(banana.key, "banana")
        self.assertEqual(banana.value, None)

    def test_traverse_to_parent_with_arrow(self):
        green = self.tree["fruits"]["green"]["apple"]["__<-__"]
        self.assertEqual(green.key,"green")    



if __name__ == "__main__":
    unittest.main()