# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        v = root.val
        def check(node, v):
            if node.val != v:
                return False
            if node.left:
                lr = check(node.left, v)
                if not lr:
                    return False
            if node.right:
                lr = check(node.right, v)
                if not lr:
                    return False    
            return True 
        return check(root, v)    