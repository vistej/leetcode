"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return root
            
        self.r = []

        def loo(n):
            self.r.append(n.val)
            if n.children:
                for c in n.children:
                    loo(c)
        
        loo(root)

        return self.r
