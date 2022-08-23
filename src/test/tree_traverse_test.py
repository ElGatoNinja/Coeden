import unittest
from value_tree import ValueNode

class TraverseTree(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = ValueNode("root")
        self.tree.new_leaf("fruits")
        self.tree["fruits"].new_leaf("red")
        self.tree["fruits"].new_leaf("yellow")
        self.tree["fruits"].new_leaf("purple")
        self.tree["fruits"].new_leaf("green")
        
        self.tree["fruits"]["red"].new_leaf("apple")
        self.tree["fruits"]["red"].new_leaf("strawberry")

        self.tree["fruits"]["yellow"].new_leaf("banana")
        self.tree["fruits"]["yellow"].new_leaf("pineapple")
        
        self.tree["fruits"]["purple"].new_leaf("berry")

        self.tree["fruits"]["green"].new_leaf("pear")
        self.tree["fruits"]["green"].new_leaf("apple")

        self.tree.new_leaf("tech companies")
        self.tree["tech companies"].new_leaf("apple", 345)
        self.tree["tech companies"].new_leaf("microsoft", 243)
        self.tree["tech companies"].new_leaf("google",348)
        self.tree["tech companies"].new_leaf("meta",145)


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

    def test_one_level_wildcard(self):
        berry = self.tree["fruits"]["__*__"]["berry"].tolist()
        self.assertEqual(len(berry), 1)
        self.assertEqual(berry[0].key, "berry")
        self.assertEqual(berry[0]["__<-__"].key, "purple")
    
    def test_wildcard_first_or_nonode(self):
        berry = self.tree["fruits"]["__*__"]["berry"]["__?__"]
        mango = self.tree["fruits"]["__*__"]["mango"]["__?__"]

        self.assertEqual(berry.key, "berry")
        self.assertEqual(mango,None)

if __name__ == "__main__":
    unittest.main()
