# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dep(node):
            l = None
            if node.left:
                l = dep(node.left) + 1
            if node.right:
                k = dep(node.right) + 1
                l = min(k, l) if l else k
            return l if l else 1
        
        return dep(root)