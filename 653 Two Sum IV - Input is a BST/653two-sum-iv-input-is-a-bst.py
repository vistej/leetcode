# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        d = {}

        def loo(n):
            if not n:
                return False
            if n.val in d:
                return True
            d[k - n.val] = True
            a = loo(n.left)
            b = loo(n.right)
            return a or b

        return loo(root)
