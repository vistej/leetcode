"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.m = 0

        def loo(n, c):
            c += 1
            if n.children:
                for k in n.children:
                    loo(k, c)
            else:
                self.m = max(self.m, c)
        if root:
            loo(root, 0)

        return self.m