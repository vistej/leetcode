# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.r = 0

        def loo(n, k):
            k += str(n.val)

            if n.left:
                loo(n.left, k)
            if n.right:
                loo(n.right, k)

            if not n.left and not n.right:
                self.r +=  int(k, 2)
        
        loo(root, '')

        return self.r