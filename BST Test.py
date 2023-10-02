import unittest

from BST import BST

class BSTTestCase(unittest.TestCase):
    def setUp(self):
        """
        NOTE: This gets run before EACH test method.
        :return:
        """
        print("Setting up.")
        self.BST1 = BST()
        self.BST1.add("magenta");
        self.BST1.add("green");
        self.BST1.add("orange");
        self.BST1.add("blue");
        self.BST1.add("yellow");
        self.BST1.add("turquoise");
        self.BST1.add("teal");
        self.BST1.add("black");
        self.BST1.add("pink");
        self.BST1.add("white");
        self.BST1.add("purple");
        self.BST1.add("gold");

    def test0_repr(self):
        print("============================ Test 0:")
        print("Checking that our tree loaded correctly and represents the alphabetized list.")
        self.BST1.printTree()
        self.assertEqual("[black, blue, gold, green, magenta, orange, pink, purple, teal, turquoise, white, yellow]", self.BST1.__repr__())

    def test1_duplicate_managed(self):
        print("============================ Test 1:")
        print("Checking that attempting to add a duplicate item does returns false and does not change the list.")
        self.assertFalse(self.BST1.add("magenta"))
        self.assertFalse(self.BST1.add("pink"))
        self.assertFalse(self.BST1.add("gold"))
        self.assertEqual("[black, blue, gold, green, magenta, orange, pink, purple, teal, turquoise, white, yellow]",
                         self.BST1.__repr__())
        self.assertTrue(self.BST1.add("ultraviolet"))

    def test2_contains(self):
        print("============================ Test 2:")
        print("Checking whether items are in the tree or not.")
        self.assertTrue(self.BST1.__contains__("magenta"))
        self.assertTrue("magenta" in self.BST1) # "in" is alternate way of calling special method __contains__
        self.assertTrue("gold" in self.BST1)
        self.assertTrue("teal" in self.BST1)
        self.assertTrue("purple" in self.BST1)
        self.assertFalse("maroon" in self.BST1)
        self.assertFalse("pinkish" in self.BST1)
        self.assertFalse("amber" in self.BST1)
        self.assertFalse("Zircon" in self.BST1)

    def test3_remove_missing_item(self):
        print("============================ Test 3:")
        print("Attempting to remove an item not found in the BST.")
        self.assertFalse(self.BST1.removeItem("cyan"),"Removing cyan should return false, since cyan is not in BST1.")
        self.assertEqual("[black, blue, gold, green, magenta, orange, pink, purple, teal, turquoise, white, yellow]",
                         self.BST1.__repr__(),
                         "BST contents should be unchanged.")

    def test4_remove_leaf(self):
        print ("============================ Test 4:")
        self.BST1.printTree()
        print("Removing 'gold.'")
        self.assertTrue(self.BST1.removeItem("gold"), "Removing 'gold' should return true.");
        self.BST1.printTree()
        self.assertEqual("[black, blue, green, magenta, orange, pink, purple, teal, turquoise, white, yellow]",
                         self.BST1.__repr__(),
                         "BST contents should only be missing gold.")
        print("Removing 'purple.")
        self.assertTrue(self.BST1.removeItem("purple"));
        self.BST1.printTree()
        self.assertEqual("[black, blue, green, magenta, orange, pink, teal, turquoise, white, yellow]",self.BST1.__repr__())

    def test5_remove_last_item_from_tree(self):
        print("============================ Test 5:")
        BST2 = BST()
        BST2.add("aquamarine")
        self.assertTrue(BST2.removeItem("aquamarine"))
        self.assertEqual("[]",BST2.__repr__())

    def test6_remove_node_with_one_child(self):
        print("============================ Test 6:")
        self.BST1.printTree()
        print("Removing 'pink.'")
        self.assertTrue(self.BST1.removeItem("pink"))
        self.BST1.printTree()
        self.assertEqual("[black, blue, gold, green, magenta, orange, purple, teal, turquoise, white, yellow]", self.BST1.__repr__())

        print("Removing 'orange.'")
        self.assertTrue(self.BST1.removeItem("orange"))
        self.BST1.printTree()
        self.assertEqual("[black, blue, gold, green, magenta, purple, teal, turquoise, white, yellow]", self.BST1.__repr__())

        print("Removing 'green.'")
        self.assertTrue(self.BST1.removeItem("green"))
        self.BST1.printTree()
        self.assertEqual("[black, blue, gold, magenta, purple, teal, turquoise, white, yellow]", self.BST1.__repr__())

    def test7_remove_root_with_one_child(self):
        print("============================ Test 4:")
        BST3 = BST()
        BST3.add("lemon")
        BST3.add("marigold")
        BST3.printTree()
        self.assertTrue(BST3.removeItem("lemon"))
        BST3.printTree()
        self.assertEqual("[marigold]", BST3.__repr__())

        BST4 = BST()
        BST4.add("silver")
        BST4.add("bronze")
        BST4.printTree()
        self.assertTrue(BST4.removeItem("silver"))
        BST4.printTree()
        self.assertEqual("[bronze]", BST4.__repr__())

    def test8_remove_node_with_two_children(self):
        print("============================ Test 8:")
        self.BST1.printTree()
        print("Removing 'blue.'")
        self.assertTrue(self.BST1.removeItem("blue"))
        self.BST1.printTree()
        self.assertEqual("[black, gold, green, magenta, orange, pink, purple, teal, turquoise, white, yellow]",
                         self.BST1.__repr__())

        print("Removing 'turquoise.'")
        self.assertTrue(self.BST1.removeItem("turquoise"))
        self.BST1.printTree()
        self.assertEqual("[black, gold, green, magenta, orange, pink, purple, teal, white, yellow]",
                         self.BST1.__repr__())

    def test9_remove_root_with_two_children(self):
        print("============================ Test 9:")
        self.BST1.printTree()
        print("Removing 'magenta.'")
        self.assertTrue(self.BST1.removeItem("magenta"))
        self.BST1.printTree()
        self.assertEqual("[black, blue, gold, green, orange, pink, purple, teal, turquoise, white, yellow]",
                         self.BST1.__repr__())