# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            dummy = ListNode(0, head)
            current = head 
            previous = dummy
            for _ in range(n):
                current = current.next
            while current :
                current = current.next
                previous = previous.next
            previous.next = previous.next.next
            return dummy.next

           
            
            
           
