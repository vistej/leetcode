# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None

        def loop(node):
            if not node or self.res:
                return

            if p.val <= node.val <= q.val or p.val >= node.val >= q.val:
                self.res = node
                return
            elif p.val >= node.val and q.val >= node.val:
                loop(node.right)
            else:
                loop(node.left)
        
        loop(root)

        return self.res
            
