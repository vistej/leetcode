# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = {}
        no = {}
        for de in descriptions:
            n = d[de[0]] if de[0] in d else TreeNode(de[0])
            if not de[0] in no:
                no[de[0]] = True
            c = d[de[1]] if de[1] in d else TreeNode(de[1])
            d[de[1]] = c
            no[de[1]] = False
            if de[2]:
                n.left = c
            else:
                n.right = c
            d[de[0]] = n
        for k in no.keys():
            if no[k]:
                return d[k]