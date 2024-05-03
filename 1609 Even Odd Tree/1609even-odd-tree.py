# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        a = [root]
        l = 0

        def iseven(v):
            return v % 2 == 0

        def isodd(v):
            return v % 2 == 1

        while len(a):
            r = []
            p = None
            for n in a:
                if iseven(l):
                    if isodd(n.val):
                        if p and p >= n.val:
                            return False
                        p = n.val
                    else:
                        return False
                else:
                    if iseven(n.val):
                        if p and p <= n.val:
                            return False
                        p = n.val
                    else:
                        return False
                if n.left:
                    r.append(n.left)
                if n.right:
                    r.append(n.right)
            a = r
            l += 1
        
        return True