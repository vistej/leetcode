# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def loop(node):
            if not node:
                return 0, 0
            
            x, m1 = loop(node.left)
            y, m2 = loop(node.right)
            res = x + y

            return 1 + max(x, y), max(m1, m2, res)
        
        _, res = loop(root)
        return res