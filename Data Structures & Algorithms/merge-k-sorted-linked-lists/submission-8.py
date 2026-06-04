# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # O(Nlogk) (N = total number of nodes across all lists, k = number of lists)Space complexity: O(1) (auxiliary space, excluding the output)
        
        if lists == None or len(lists) == 0:
            return None
        
        while(len(lists) > 1):
            mergedLists = []
            for i in range(0, len(lists), 2):
                mergedLists.append(self._mergeLists(lists[i],lists[i+1] if i+1 < len(lists) else None))
            lists=mergedLists
        return lists[0]
          

    def _mergeLists(self,p1,p2):
        dummy = ListNode()  
        tail = dummy
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

        