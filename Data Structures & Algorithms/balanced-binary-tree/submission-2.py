# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return (True,0)
            lb,left_de= dfs(root.left)
            rb,right_de=dfs(root.right)
            balanced = lb and rb and (abs(left_de - right_de)  <= 1)
            return (balanced , 1 +max(left_de ,right_de))
        a , b = dfs(root)
        return a
        
   
        