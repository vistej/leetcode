# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def loo(n):
            r = []
            if n.left:
                r = loo(n.left)
            if n.right:
                r.extend(loo(n.right))
            if r:
                r = [str(n.val) + '->' + i for i in r]
            else:
                r = [str(n.val)]
            return r
        
        return loo(root)
