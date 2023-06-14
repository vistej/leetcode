# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        def searchTree(node):
            if not node:
                return
            if node.left:
                searchTree(node.left)
            arr.append(node.val)
            if node.right:
                searchTree(node.right)
        
        searchTree(root)
        mv = abs(arr[0] - arr[1])
        for i in range(len(arr) -1):
            mv = min(mv, abs(arr[i] - arr[i + 1]))

        return mv