# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        a = [(0, root)]
        d = {}
        i = 0
        while i < len(a):
            l,n = a[i]
            d[l] = d.get(l, 0) + n.val
                
            if n.left:
                a.append((l + 1, n.left))
            if n.right:
                a.append((l + 1, n.right))
            i += 1
        
        k = a[-1][0]
        return d[k]
