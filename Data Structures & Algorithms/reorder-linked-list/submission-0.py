# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            l1 = head
            l2 = slow.next           
            slow.next = None
            prev = None
            current = l2
            while current:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            l2 = prev       
            p1, p2 = l1, l2
            while p2:
                tmp1 = p1.next                
                tmp2 = p2.next
                p1.next = p2
                p2.next = tmp1
                p1 = tmp1
                p2 = tmp2
          

            
            
                


        