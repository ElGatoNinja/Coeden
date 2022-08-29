import unittest
from coeden import ValueNode
from coeden.specialClasses.base_node import NoNode

class NoNodes(unittest.TestCase):
    def test_get_unexistent_node_returns_nonode(self):
        tree = ValueNode("root")
        is_nonode = isinstance(tree["ghost node"],NoNode)
        self.assertEqual(is_nonode, True)
    
    def test_nonode_is_None(self):
        tree = ValueNode("root")
        self.assertEqual(tree["unexistent node"], None)
        self.assertEqual(tree["unexistent node"].key, None)
        self.assertEqual(tree["unexistent node"].value, None)

    def test_chained_nonodes(self):
        tree = ValueNode("root")
        nonode = tree["unexisting node"]["ghost node"]["magic node"]
        is_nonode = isinstance(nonode,NoNode)
        self.assertEqual(is_nonode, True)

    def test_add_nonode(self):
        tree = ValueNode("root")
        tree["ethereal node"].create_all()
        self.assertEqual(tree["ethereal node"].key, "ethereal node")

    def test_add_multiple_nonodes(self):
        tree = ValueNode("root")
        tree["new 1"]["new 2"].create_all()

        self.assertEqual(tree["new 1"]["new 2"].key, "new 2")
        self.assertEqual(tree["new 1"]["new 2"]["__<-__"].key, "new 1")

    def test_nonodes_are_falsey(self):
        tree = ValueNode("root")
        self.assertFalse(tree["unexistent 1"]["unexistent 2"])
    
    def test_nodes_are_truthy(self):
        tree = ValueNode("root")
        tree.new_leaf("existent 1")
        self.assertTrue(tree["existent 1"])


if __name__ == "__main__":
    unittest.main()
