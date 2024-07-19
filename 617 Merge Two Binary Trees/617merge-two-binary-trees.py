# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def loo(a, b):
            if not a:
                return b
            if not b:
                return a
            
            n = TreeNode(a.val + b.val)
            n.left = loo(a.left, b.left)
            n.right = loo(a.right, b.right)
            return n

        
        return loo(root1, root2)