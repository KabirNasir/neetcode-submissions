# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue =deque()
        lis = []
        if root:
            queue.append(root)        
        while len(queue) > 0:
            for i in range(len(queue)):                
                curr = queue.popleft()
                last_val = curr.val          
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if last_val is not None:       
                lis.append(last_val)
            
        return lis