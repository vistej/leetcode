# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def doit(node):
            if node:
                doit(node.right)
                doit(node.left)
                node.right, node.left = node.left, node.right
        doit(root)
        return root
