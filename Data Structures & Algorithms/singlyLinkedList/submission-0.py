from typing import List

class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


class LinkedList:

    def __init__(self):
        self.head = ListNode(-1) 
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val, self.head.next)
        self.head.next = newNode

        if self.size == 0:
            self.tail = newNode

        self.size += 1

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        prev = self.head
        for _ in range(index):
            prev = prev.next

        toDelete = prev.next
        prev.next = toDelete.next

        if toDelete == self.tail:
            self.tail = prev

        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        cur = self.head.next
        res = []

        while cur:
            res.append(cur.val)
            cur = cur.next

        return res