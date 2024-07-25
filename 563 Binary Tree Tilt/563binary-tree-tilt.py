# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.r = 0

        def loo(n):
            if not n:
                return 0
            ls = loo(n.left)
            rs = loo(n.right)
            self.r += abs(ls - rs)
            return ls + rs + n.val
        if root:
            loo(root)
        return self.r