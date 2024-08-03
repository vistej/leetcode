# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        a = set()

        b = [root]
        i = 0
        while i < len(b):
            n = b[i]
            a.add(n.val)
            if n.left:
                b.append(n.left)
                b.append(n.right)
            i += 1
        return sorted(a)[1] if len(a) > 1 else -1