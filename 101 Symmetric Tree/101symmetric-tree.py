# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(na, nb):
            if na and nb:
                return na.val==nb.val and dfs(na.left, nb.right) and dfs(na.right, nb.left)
            elif not na and not nb:
                return True
            return False
        return dfs(root, root)
