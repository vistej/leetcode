# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        bluh = {}
        def goNode(level, node):
            if not node:
                return
            if not level in bluh:
                bluh[level] = []
            bluh[level].append(node.val)
            goNode(level + 1, node.left)
            goNode(level + 1, node.right)
        goNode(1, root)
        res = (1, sum(bluh[1]))
        for i in range(2, len(bluh) + 1):
            bll = sum(bluh[i])
            if bll > res[1]:
                res = (i, bll)
        return res[0]
