# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        def loop(node, m):
            if not node:
                return
            if node.val >= m:
                res[0] += 1
                m = node.val
            loop(node.left, m)
            loop(node.right, m)
        
        loop(root, float('-inf'))
        return res[0]