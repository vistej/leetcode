# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        a = []

        def loo(n):
            if n.left:
                loo(n.left)
            a.append(n.val)
            if n.right:
                loo(n.right)
        if root1:
            loo(root1)
        if root2:
            loo(root2)
        a.sort()
        return a