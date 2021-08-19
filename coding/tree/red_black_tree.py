from enum import Enum

class Color(Enum):
    BLACK = 1
    RED = 2

class Node:

    def __init__(self, val, left=None, right=None, parent=None, color=Color.BLACK):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color

    def min(self):
        cur = self
        while cur.left and cur.left != NIL:
            cur = cur.left
        return cur

NIL = Node(None)

class RedBlackTree:
    """
    Here are Red-Black Tree properties:
    1) Every node is either red or black
    2) Root node is always black
    3) Every leaf node (NIL) is always black
    4) If a node is red, both its children are black
    5) For each node, all simple paths from the node to descendant leaves contain the same number of black nodes
    """

    def __init__(self, root=NIL):
        self.root = root

    def add(self, val):
        prev = NIL
        cur = self.root
        while cur != NIL:
            prev = cur
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        node = Node(val, left=NIL, right=NIL, parent=prev, color=Color.RED)
        if prev == NIL:
            self.root = node
        elif val < prev.val:
            prev.left = node
        else:
            prev.right = node
        self.__fixup_insert(node)

    def __fixup_insert(self, node):
        while node.parent.color == Color.RED:
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == Color.RED:
                    node.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.__rotate_left(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self.__rotate_right(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.color == Color.RED:
                    node.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.__rotate_right(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self.__rotate_left(node.parent.parent)
        self.root.color = Color.BLACK

    def delete(self, z):
        if z == NIL:
            return
        y = z
        y_original_color = y.color
        if z.left == NIL:
            x = z.right
            self.__transplant(z, z.right)
        elif z.right == NIL:
            x = z.left
            self.__transplant(z, z.left)
        else:
            y = z.right.min()
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__transplant(y, x)
                y.right = z.right
                z.right.parent = y
            self.__transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == Color.BLACK:
            self.__fixup_delete(x)

    def __fixup_delete(self, x):
        while x != self.root and x.color == Color.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.__rotate_left(x.parent)
                    w = x.parent.right
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.right.color == Color.BLACK:
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self.__rotate_right(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self.__rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.__rotate_right(x.parent)
                    w = x.parent.left
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.left.color == Color.BLACK:
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self.__rotate_left(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self.__rotate_right(x.parent)
                    x = self.root
        x.color = Color.BLACK

    def __transplant(self, u, v):
        if u.parent == NIL:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def __rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == NIL:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def __rotate_right(self, y):
        x = y.left
        y.left = x.right
        if x.right != NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == NIL:
            self.root = x
        elif y.parent.left == y:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x
