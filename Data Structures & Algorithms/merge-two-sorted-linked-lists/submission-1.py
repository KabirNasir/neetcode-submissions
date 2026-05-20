# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if(list1 == None and list2 == None) :
            return list1
        elif (list1 == None):
            return list2
        elif (list2 == None):
            return list1
        else :
            list3 = ListNode(-1)
            p1 = list1
            p2 = list2
            p3 = list3
            while p1 and p2:
                
                if(p1.val < p2.val):
                    p3.next = ListNode(p1.val)
                    p3 = p3.next
                    p1= p1.next
                elif p1.val > p2.val :
                    p3.next = ListNode(p2.val)
                    p3 = p3.next
                    p2= p2.next
                else: 
                    p3.next = ListNode(p1.val)
                    p3 = p3.next
                    p3.next = ListNode(p2.val)
                    p3 = p3.next
                    p1= p1.next
                    p2= p2.next
            if p1:
                p3.next = p1
            elif p2:
                p3.next = p2
            return list3.next

                
            


        
        