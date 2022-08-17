import unittest
from tree import Node

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
