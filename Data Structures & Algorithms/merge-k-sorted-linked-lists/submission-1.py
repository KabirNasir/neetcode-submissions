# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ml = []
        # print(lists[0].val,lists[0].next.val,lists[0].next.next.val )
        # return None
        for i in range(len(lists)):
            p = lists[i]
            while(p!= None):
                # print(p.val)
                ml.append(p.val)
                # print(ml)
                p=p.next
        # print(ml)
        ml.sort()
        # print(ml)
        dummy = ListNode()  
        tail = dummy
        for i in ml:
            # print(i)
            tail.next = ListNode(i)
            tail = tail.next
        # print(dummy.next)
        return dummy.next

        