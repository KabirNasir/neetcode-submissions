# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:     
        count = 0
        def check(root, maxi) :
            nonlocal count
            if root is None: 
                return

            if root.val >= maxi:
                count+=1
            maxi=max(root.val , maxi)

            check(root.left, maxi)
            check(root.right, maxi)    
        check(root,root.val)
        return count