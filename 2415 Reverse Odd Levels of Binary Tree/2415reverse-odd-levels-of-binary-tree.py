# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d = [root]
        i = 1

        while d:
            k = []
            for n in d:
                if n.left:
                    k.append(n.left)
                    k.append(n.right)
            if i % 2:
                v = [p.val for p in k]
                for j in range(len(k)):
                    k[len(k) - 1 - j].val = v[j]
            i += 1
            d = k
        
        return root