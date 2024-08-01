# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        a = [(root, 0, 0)]
        i = 0

        d = None

        while i < len(a):
            n,l,p = a[i]
            if n.val == x or n.val == y:
                if d:
                    return d[0] == l and d[1] != p
                else:
                    d = (l,p)
            if n.left:
                a.append((n.left, l + 1, n.val))
            if n.right:
                a.append((n.right, l + 1, n.val))
            
            i += 1

        return False