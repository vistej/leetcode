"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return root
        c = [root]
        r = []
        while c:
            i = c.pop()
            r.append(i.val)
            for p in i.children:
                c.append(p)

        return r[::-1]
