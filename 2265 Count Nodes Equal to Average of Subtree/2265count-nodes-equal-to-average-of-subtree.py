# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.r = 0

        def loo(n):
            s = n.val
            c = 1
            if n.left:
                a,b = loo(n.left)
                s += a
                c += b
            if n.right:
                e,f = loo(n.right)
                s += e
                c += f
            if n.val == (s//c):
                self.r += 1
            return s,c
        
        loo(root)
        return self.r