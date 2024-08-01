# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        a = [root]
        t = []
        i = 0
        while i < len(a):
            t.append(a[i].val)
            if a[i].left:
                a.append(a[i].left)
            if a[i].right:
                a.append(a[i].right)
            i += 1
        

        t.sort()

        m = t[1]
        for i in range(len(t) - 1):
            m = min(m, abs(t[i + 1] - t[i]))
        
        return m
