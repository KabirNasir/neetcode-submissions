# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()  
        
        for i in range(len(lists)):
            tail = dummy
            p1, p2 = dummy.next, lists[i]

            while p1 and p2:
                if p1.val <= p2.val:
                    tail.next = p1
                    p1 = p1.next
                else:
                    tail.next = p2
                    p2 = p2.next
                tail = tail.next

            tail.next = p1 if p1 is not None else p2
        return dummy.next

        