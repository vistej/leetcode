# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.a = []
        self.b = []

        def dfs(node, path):
            if node.val == startValue:
                self.a = path.copy()
            if node.val == destValue:
                self.b = path.copy()
            if self.a and self.b:
                return
            
            if node.left:
                path.append("L")
                dfs(node.left, path)
                path.pop()
            if node.right:
                path.append("R")
                dfs(node.right, path)
                path.pop()

        dfs(root, [])  

        i = 0
        while i < len(self.b) and i < len(self.a):
            if self.a[i] != self.b[i]:
                break
            i += 1

        self.a, self.b = self.a[i:], self.b[i:]
        return "U" * len(self.a) + "".join(self.b)
        

