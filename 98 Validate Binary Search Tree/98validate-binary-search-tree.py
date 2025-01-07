# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def loop(node, l, r):
            if not node:
                return True
            if not (node.val > l and node.val < r):
                return False
            return loop(node.left, l, node.val) and loop(node.right, node.val, r)

        return loop(root, float('-inf'), float('inf'))

