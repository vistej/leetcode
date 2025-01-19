# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = [root]
        root.val = 0

        while level:
            vals = []
            nxt_lvl = []
            for node in level:
                s = 0
                if node.left:
                    s += node.left.val
                    nxt_lvl.append(node.left)
                if node.right:
                    s += node.right.val
                    nxt_lvl.append(node.right)
                vals.append(s)
            
            total = sum(vals)
            if total:
                for i in range(len(level)):
                    val = total - vals[i]
                    node = level[i]
                    if node.left:
                        node.left.val = val
                    if node.right:
                        node.right.val = val
            level = nxt_lvl

        return root
