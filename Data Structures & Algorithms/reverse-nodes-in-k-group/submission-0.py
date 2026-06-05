# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupPrev = dummy

        while True:
            tempHead= groupPrev
            for _ in range(k):
                
                tempHead = tempHead.next

                if tempHead == None:
                    return dummy.next            
            temptail = tempHead.next                       
            previous, current = temptail , groupPrev.next  
            original_first = groupPrev.next
            while current != temptail:
                temp = current.next
                current.next = previous
                previous=current
                current = temp
            
            groupPrev.next = previous
            original_first.next = temptail
            groupPrev = original_first


        return None
