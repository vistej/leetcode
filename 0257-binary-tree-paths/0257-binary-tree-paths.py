# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(n, s):
            if not n:
                return
            s += ('->' if s else '') + str(n.val)
            if not n.left and not n.right:
                res.append(s)

            dfs(n.left, s)
            dfs(n.right, s)
        
        dfs(root, '')

        return res