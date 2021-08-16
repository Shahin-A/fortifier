from unittest import TestCase, main

from coding.tree.binary_search_tree import BinarySearchTree

class TestUnboundedTree(TestCase):

    def test_predecessor_single_node(self):
        tree = BinarySearchTree(6)
        self.assertIsNone(tree.predecessor())

    def test_successor_single_node(self):
        tree = BinarySearchTree(6)
        self.assertIsNone(tree.predecessor())

    def test_predecessor_multiple_node(self):
        root = self.__get_sample_tree()
        self.assertEqual(5, root.predecessor().val)
        self.assertEqual(2, root.left.predecessor().val)
        self.assertIsNone(root.right.predecessor())

    def test_successor_multiple_node(self):
        root = self.__get_sample_tree()
        self.assertEqual(7, root.successor().val)
        self.assertEqual(5, root.left.successor().val)
        self.assertEqual(8, root.right.successor().val)

    def test_inorder(self):
        root = self.__get_sample_tree()
        self.assertEqual([2, 5, 5, 6, 7, 8], root.inorder())

    def test_preorder(self):
        root = self.__get_sample_tree()
        self.assertEqual([6, 5, 2, 5, 7, 8], root.preorder())

    def test_inorder_recursive(self):
        root = self.__get_sample_tree()
        self.assertEqual([2, 5, 5, 6, 7, 8], root.inorder_recursive())

    def test_invalid_trees(self):
        invalid_left_tree = BinarySearchTree(8,
                left=BinarySearchTree(5, right=BinarySearchTree(9)),
                right=BinarySearchTree(10))
        self.assertFalse(invalid_left_tree.valid())
        invalid_right_tree = BinarySearchTree(8,
                left=BinarySearchTree(5, right=BinarySearchTree(6)),
                right=BinarySearchTree(10, left=BinarySearchTree(1)))
        self.assertFalse(invalid_right_tree.valid())

    def test_valid_trees(self):
        self.assertTrue(BinarySearchTree(1).valid())

        root = self.__get_sample_tree()
        self.assertTrue(root.valid())

    def __get_sample_tree(self):
        left_subtree = BinarySearchTree(5, left=BinarySearchTree(2), right=BinarySearchTree(5))
        right_subtree = BinarySearchTree(7, right=BinarySearchTree(8))
        root = BinarySearchTree(6, left=left_subtree, right=right_subtree)
        return root