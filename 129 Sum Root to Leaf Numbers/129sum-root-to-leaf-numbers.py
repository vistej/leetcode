# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def loop(r):
            re = []
            if r.left:
                re.extend(loop(r.left))
            if r.right:
                re.extend(loop(r.right))
            if len(re):
                re = [str(r.val) + i for i in re]
            else:
                re.append(str(r.val))
            return re
        vals = loop(root)
        a = 0
        for v in vals:
            a += int(v)
        return a