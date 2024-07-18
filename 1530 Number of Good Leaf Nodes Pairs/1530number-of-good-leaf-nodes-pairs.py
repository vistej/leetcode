# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.c = 0

        def loo(n):
            if not n.left and not n.right:
                return [1]
            a = b = []
            if n.left:
                a = loo(n.left)
            if n.right:
                b = loo(n.right)
            r = []
            for k in a:
                r.append(k + 1)
                for l in b:
                    if k + l <= distance:
                        self.c += 1
            for l in b:
                r.append(l + 1)
            
            return r
        
        x = loo(root)

        return self.c
            
            