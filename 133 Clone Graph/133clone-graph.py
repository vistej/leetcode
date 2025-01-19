"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        res = {node.val: Node(node.val, [])}
        nodes = [node]

        while nodes:
            temp = []
            for n in nodes:
                nn = res[n.val]
                for nb in n.neighbors:
                    if nb.val and nb.val not in res:
                        res[nb.val] = Node(nb.val)
                        temp.append(nb)
                    nn.neighbors.append(res[nb.val])
            nodes = temp

        return res[node.val]

