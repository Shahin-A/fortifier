from unittest import TestCase

from coding.tree.red_black_tree import RedBlackTree, Color, NIL

class TestRedBlackTree(TestCase):

    def test_empty_tree(self):
        tree = RedBlackTree()
        self.assertEqual(NIL, tree.root)

    def test_single_node(self):
        tree = RedBlackTree()
        tree.add(1)
        self.assertEqual(Color.BLACK, tree.root.color)
        self.assertEqual(1, tree.root.val)
        self.assertEqual(NIL, tree.root.left)
        self.assertEqual(NIL, tree.root.right)

    def test_multiple_node(self):
        tree = RedBlackTree()
        tree.add(1)
        tree.add(2)
        tree.add(3)
        self.assertEqual(Color.BLACK, tree.root.color)
        self.assertEqual(2, tree.root.val)
        self.assertEqual(Color.RED, tree.root.left.color)
        self.assertEqual(1, tree.root.left.val)
        self.assertEqual(Color.RED, tree.root.right.color)
        self.assertEqual(3, tree.root.right.val)

        tree.add(2)
        self.assertEqual(Color.BLACK, tree.root.color)
        self.assertEqual(2, tree.root.val)
        self.assertEqual(Color.BLACK, tree.root.left.color)
        self.assertEqual(1, tree.root.left.val)
        self.assertEqual(Color.BLACK, tree.root.right.color)
        self.assertEqual(3, tree.root.right.val)
        self.assertEqual(Color.RED, tree.root.right.left.color)
        self.assertEqual(2, tree.root.right.left.val)