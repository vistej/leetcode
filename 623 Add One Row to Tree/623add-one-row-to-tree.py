# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        hc = root
        k = 1
        ke = [root]
        while k < depth - 1:
            ar = []
            for v in ke:
                if v.left:
                    ar.append(v.left)
                if v.right:
                    ar.append(v.right)
            ke = ar
            k += 1

        for v in ke:
            temp = None
            if v.left:
                temp = v.left
            v.left = TreeNode(val)
            if temp:
                x = v.left
                x.left = temp
            temp = None
            if v.right:
                temp = v.right
            v.right = TreeNode(val)
            if temp:
                x = v.right
                x.right = temp
        return root