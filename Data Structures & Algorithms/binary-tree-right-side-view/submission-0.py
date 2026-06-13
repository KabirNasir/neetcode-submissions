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
        
        level = 0
        while len(queue) > 0:
            skew = []
            for i in range(len(queue)):
                
                curr = queue.popleft()
                skew.append(curr.val)
                print(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                print(skew)
            lis.append(skew[-1])
            
            level+=1
        print(lis)
        return lis