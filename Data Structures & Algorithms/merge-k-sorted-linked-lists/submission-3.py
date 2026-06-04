# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Time complexity: O(NlogN)Space complexity: O(N)
        ml = []
        for i in range(len(lists)):
            p = lists[i]
            while(p!= None):
                ml.append(p.val)
                p=p.next
        ml.sort()
        dummy = ListNode()  
        tail = dummy
        for i in ml:
            tail.next = ListNode(i)
            tail = tail.next
        return dummy.next

        