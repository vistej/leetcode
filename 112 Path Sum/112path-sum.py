# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def loo(n, v):
            v += n.val
            if not n.left and not n.right:
                return v == targetSum
            r = False
            if n.left:
                r = r or loo(n.left, v)
            if n.right:
                r = r or loo(n.right, v)
            return r
        
        return loo(root, 0)
