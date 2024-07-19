# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.r = None
        def loo(n):
            if n.val == target.val:
                self.r = n
                return
            if not self.r and n.left:
                loo(n.left)
            if not self.r and n.right:
                loo(n.right)
            return
        
        loo(cloned)
        return self.r
