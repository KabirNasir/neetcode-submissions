# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # s = head
        while  head and head.val == val:
            head = head.next
      
        s = head 
        prev = None
        while(s):
            if(s and s.val == val):
                prev.next = s.next
            else:
                prev = s
            s = s.next
        return head
        