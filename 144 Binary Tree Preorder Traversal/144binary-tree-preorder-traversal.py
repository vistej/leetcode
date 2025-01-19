# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.r = []
        def loo(n):
            self.r.append(n.val)
            if n.left:
                loo(n.left)
            if n.right:
                loo(n.right)
        if root:
            loo(root)

        return self.r