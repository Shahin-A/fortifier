from unittest import TestCase

from coding.list.linked_list import LinkedList

class TestLinkedList(TestCase):

    def test_remove_last(self):
        linked_list = LinkedList(1, next=LinkedList(2, next=LinkedList(3)))
        result = linked_list.remove_Nth(1)
        self.assertEqual(str(result), "[1, 2]")

    def test_remove_first(self):
        linked_list = LinkedList(1, next=LinkedList(2, next=LinkedList(3)))
        result = linked_list.remove_Nth(3)
        self.assertEqual(str(result), "[2, 3]")