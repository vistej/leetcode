# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        data = {}

        def findIt(node):
            if node.left:
                findIt(node.left)
            if node.right:
                findIt(node.right)
            if not node.val in data:
                data[node.val] = 1
            else:
                data[node.val] += 1
        findIt(root)
        res = []
        count = 0
        for i in data.keys():
            if data[i] == count:
                res.append(i)
            if data[i] > count:
                count = data[i]
                res = [i]
        return res
