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

NIL = Node(None)

class RedBlackTree:

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
        self.__fixup(node)

    def __fixup(self, node):
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
