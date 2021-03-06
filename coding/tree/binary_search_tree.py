class BinarySearchTree:

    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

    def flatten(self):
        stack = []
        stack.append(self)
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            if stack:
                node.right = stack[-1]

            node.left = None

    def inorder(self):
        """
        Morris Inorder tree traversal.
        Creating links between predecessor and the current node to traverse the tree
        :return: a list of in order elements within the tree
        """
        inorder, cur = [], self
        while (cur):
            if (not cur.left):
                inorder.append(cur.val)
                cur = cur.right
            else:
                predecessor = cur.__predecessor()
                if (not predecessor.right):
                    predecessor.right = cur
                    cur = cur.left
                else:
                    predecessor.right = None
                    inorder.append(cur.val)
                    cur = cur.right
        return inorder

    def preorder(self):
        """
        Morris preorder tree traversal
        :return: a list of pre order elements within the BST.
        """
        preorder, cur = [], self
        while(cur):
            if (not cur.left):
                preorder.append(cur.val)
                cur = cur.right
            else:
                predecessor = cur.__predecessor()
                if (not predecessor.right):
                    predecessor.right = cur
                    preorder.append(cur.val)
                    cur = cur.left
                else:
                    predecessor.right = None
                    cur = cur.right
        return preorder

    def inorder_recursive(self):
        inorder = []
        inorder = inorder + self.left.inorder_recursive() if self.left else inorder
        inorder.append(self.val)
        inorder = inorder + self.right.inorder_recursive() if self.right else inorder
        return inorder

    def predecessor(self):
        if (self.left):
            return self.left.max()
        cur, parent = self, self.parent
        while(parent and parent.left == cur):
            cur = parent
            parent = parent.parent
        return parent

    def successor(self):
        if (self.right):
            return self.right.min()
        cur, parent = self, self.parent
        while(parent and parent.right == cur):
            cur = parent
            parent = parent.parent
        return parent

    def min(self):
        cur = self
        while (cur.left):
            cur = cur.left
        return cur

    def max(self):
        cur = self
        while(cur.right):
            cur = cur.right
        return cur

    def search(self, key):
        cur = self
        while(cur and cur.val != key):
            if (cur.val > key):
                cur = cur.left
            else:
                cur = cur.right
        return cur

    def add(self, key):
        cur, next = None, self
        while next:
            cur = next
            next = cur.left if key <= cur.val else cur.right
        if key <= cur.val:
            cur.left = BinarySearchTree(key, parent=cur)
        else:
            cur.right = BinarySearchTree(key, parent=cur)

    def delete(self, key):
        if key < self.val:
            return BinarySearchTree(self.val, left=self.left.delete(key), right=self.right, parent=self) if self.left else self
        elif key > self.val:
            return BinarySearchTree(self.val, left=self.left, right=self.right.delete(key), parent=self) if self.right else self
        else:
            if not self.left:
                return BinarySearchTree.__convert_parent(self.right, self)
            elif not self.right:
                return BinarySearchTree.__convert_parent(self.left, self)
            else:
                successor = self.right.min()
                if successor == self.right:
                    return BinarySearchTree(successor.val, left=self.left, right=successor.right, parent=self.parent)
                else:
                    right_child = BinarySearchTree.__convert_parent(self.right.delete(successor.val), self.parent)
                    return BinarySearchTree(successor.val, left=self.left, right=right_child)

    @classmethod
    def __convert_parent(cls, root, parent):
        if not root:
            return None
        return BinarySearchTree(root.val, left=root.left, right=root.right, parent=parent)


    def valid(self):

        def __valid(tree):
            valid, max_value, min_value = True, tree.val, tree.val
            if (tree.left):
                left_branch_validity, left_branch_max, left_branch_min = __valid(tree.left)
                valid = valid and left_branch_validity and tree.val >= left_branch_max
                max_value = max(tree.val, left_branch_max)
                min_value = min(tree.val, left_branch_min)
            if (tree.right):
                right_branch_validity, right_branch_max, right_branch_min = __valid(tree.right)
                valid = valid and right_branch_validity and tree.val <= right_branch_min
                max_value = max(tree.val, right_branch_max)
                min_value = min(tree.val, right_branch_min)
            return valid, max_value, min_value

        return __valid(self)[0]

    def __predecessor(self):
        predecessor = self.left
        while(predecessor and predecessor.right and predecessor.right != self):
            predecessor = predecessor.right
        return predecessor

    def __successor(self):
        successor = self.right
        while(successor and successor.left and successor.left != self):
            successor = successor.left
        return successor