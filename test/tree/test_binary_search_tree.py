from unittest import TestCase, main

from coding.tree.binary_search_tree import BinarySearchTree

class TestUnboundedTree(TestCase):

    def test_flatten(self):
        tree = self.__get_sample_tree()
        tree.flatten()
        self.assertEqual(6, tree.val)
        self.assertIsNone(tree.left)
        self.assertEqual(5, tree.right.val)
        self.assertIsNone(tree.right.left)
        self.assertEqual(2, tree.right.right.val)
        self.assertIsNone(tree.right.right.left)
        self.assertEqual(5, tree.right.right.right.val)
        self.assertIsNone(tree.right.right.right.left)
        self.assertEqual(7, tree.right.right.right.right.val)
        self.assertIsNone(tree.right.right.right.right.left)
        self.assertEqual(8, tree.right.right.right.right.right.val)
        self.assertIsNone(tree.right.right.right.right.right.left)

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
        self.assertEqual(6, root.right.predecessor().val)

    def test_successor_multiple_node(self):
        root = self.__get_sample_tree()
        self.assertEqual(7, root.successor().val)
        self.assertEqual(5, root.left.successor().val)
        self.assertEqual(8, root.right.successor().val)
        self.assertEqual(6, root.left.right.successor().val)
        self.assertIsNone(root.right.right.successor())

    def test_inorder(self):
        root = self.__get_sample_tree()
        self.assertEqual([2, 5, 5, 6, 7, 8], root.inorder())

    def test_preorder(self):
        root = self.__get_sample_tree()
        self.assertEqual([6, 5, 2, 5, 7, 8], root.preorder())

    def test_inorder_recursive(self):
        root = self.__get_sample_tree()
        self.assertEqual([2, 5, 5, 6, 7, 8], root.inorder_recursive())

    def test_delete_single_node(self):
        tree = BinarySearchTree(1)
        self.assertIsNone(tree.delete(1))
        self.assertEqual(tree, tree.delete(2))

    def test_delete_multi_node(self):
        root = self.__get_sample_tree()
        root_deleted = root.delete(6)
        self.assertEqual([7, 5, 2, 5, 8], root_deleted.preorder())

        deleted = root.delete(5)
        self.assertEqual([6, 5, 2, 7, 8], deleted.preorder())


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

    def search_existing_val(self):
        root = self.__get_sample_tree()
        self.assertEqual(8, root.search(8).val)

    def search_non_existing_val(self):
        root = self.__get_sample_tree()
        self.assertIsNone(root.search(6.5))

    def __get_sample_tree(self):
        tree2 = BinarySearchTree(2)
        tree5 = BinarySearchTree(5)
        tree8 = BinarySearchTree(8)
        left_subtree = BinarySearchTree(5, left=tree2, right=tree5)
        right_subtree = BinarySearchTree(7, right=tree8)
        root = BinarySearchTree(6, left=left_subtree, right=right_subtree)
        left_subtree.parent = root
        right_subtree.parent = root
        tree2.parent = left_subtree
        tree5.parent = left_subtree
        tree8.parent = right_subtree
        return root