# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        a = [root]
        e = []
        r = 0
        i = 0
        while i < len(a):
            n = a[i]
            ev = n.val % 2 == 0
            if n.left:
                a.append(n.left)
                if ev:
                    e.append(n.left)
            if n.right:
                a.append(n.right)
                if ev:
                    e.append(n.right)
            i += 1
        
        for n in e:
            if n.left:
                r += n.left.val
            if n.right:
                r += n.right.val
        
        return r