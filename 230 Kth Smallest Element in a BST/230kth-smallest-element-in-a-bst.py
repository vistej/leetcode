# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def loop(node):
            if not node:
                return []
            
            l = loop(node.left)
            l.append(node.val)
            r = loop(node.right)
            return l + r
        
        res = loop(root)

        return res[k - 1]
