# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.r = 0

        def loo(n):
            self.r += 1
            if n.left:
                loo(n.left)
            if n.right:
                loo(n.right)
        if root:
            loo(root)

        return self.r

