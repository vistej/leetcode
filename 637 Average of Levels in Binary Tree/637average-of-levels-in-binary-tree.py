# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        a = [root]
        r = []

        while len(a):
            c = []
            s = 0
            i = 0
            for v in a:
                s += v.val
                i += 1
                if v.left:
                    c.append(v.left)
                if v.right:
                    c.append(v.right)
            r.append(s/i)
            a = c

        return r
