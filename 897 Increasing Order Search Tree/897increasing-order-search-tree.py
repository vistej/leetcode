# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.r = None
        self.rc = None

        def loo(n):
            if n.left:
                loo(n.left)
            if not self.r:
                self.r = TreeNode(n.val)
                self.rc = self.r
            else:
                self.rc.right = TreeNode(n.val)
                self.rc = self.rc.right
            if n.right:
                    loo(n.right)
        
        loo(root)
        return self.r