# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.m = 0

        def loo(node, de, di):
            self.m = max(self.m, de)

            if node.left:
                if di != "l":
                    loo(node.left, de + 1, 'l')
                else:
                    loo(node.left, 1, 'l')
            if node.right:
                if di != 'r':
                    loo(node.right, de + 1, 'r')
                else:
                    loo(node.right, 1, 'r')
        loo(root, 0, "")

        return self.m
