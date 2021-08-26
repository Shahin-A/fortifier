class LinkedList:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def remove_Nth(self, n):
        cur, next, i = None, self, 0
        while i < n:
            next = next.next
            i += 1

        while next:
            next = next.next
            cur = cur.next if cur else self

        if cur:
            cur.next = cur.next.next
            return self
        else:
            return self.next

    def __str__(self):
        cur = self
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return str(arr)