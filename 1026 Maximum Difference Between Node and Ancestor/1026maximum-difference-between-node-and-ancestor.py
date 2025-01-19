# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        mi = root.val
        ma = root.val
        def loop(n, h, l):
            if n.val > h:
                h = n.val
            elif n.val < l:
                l = n.val
            
            m = h - l
            if n.left:
                lm = loop(n.left, h, l)
                m = max(m, lm)
            if n.right:
                rm = loop(n.right, h, l)
                m = max(m, rm)
            return m
            
        return loop(root, ma, mi)