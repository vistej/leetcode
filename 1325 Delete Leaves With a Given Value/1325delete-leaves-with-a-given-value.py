# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def rid(node):
            if node.left:
                c = rid(node.left)
                if c:
                    node.left = None
            if node.right:
                c = rid(node.right)
                if c:
                    node.right = None
            return node.left == None and node.right == None and node.val == target

        k = root
        rid(k)
        if root.left == None and root.right == None and root.val == target:
            return None
        return root 