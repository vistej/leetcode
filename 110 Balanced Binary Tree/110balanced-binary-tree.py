# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def loop(node):
            if not node:
                return 0, True
            x, r1 = loop(node.left)
            y, r2 = loop(node.right)
            if not r1 or not r2:
                return 0, False
            res = False
            if 0 <= abs(x - y) < 2:
                res = True
            return 1 + max(x, y), res
        
        _, res = loop(root)

        return res