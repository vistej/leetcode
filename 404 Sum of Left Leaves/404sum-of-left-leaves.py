# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        r = 0
        if root.left and not root.left.left and not root.left.right:
            r += root.left.val
        if root.left:
            r += self.sumOfLeftLeaves(root.left)
        if root.right:
            r += self.sumOfLeftLeaves(root.right)
        return r