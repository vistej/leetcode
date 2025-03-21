# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def loop(node, level):
            if not node:
                return
            if len(res) < level:
                res.append([])
            res[level - 1].append(node.val)

            if node.left:
                loop(node.left, level + 1)
            if node.right:
                loop(node.right, level + 1)

        loop(root, 1)
            
        return res