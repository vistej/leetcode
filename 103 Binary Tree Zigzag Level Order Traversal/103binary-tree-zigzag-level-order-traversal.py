# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        tor = False
        arr = [root]
        fr = [[root.val]]
        while len(arr):
            na = []
            fa = []
            for a in arr:
                if a.left:
                    na.append(a.left)
                if a.right:
                    na.append(a.right)
            if len(na):   
                if tor:
                    tor = False
                    for a in na:
                        fa.append(a.val)
                else:
                    tor = True
                    for a in range(len(na) -1, -1, -1):
                        fa.append(na[a].val)
                fr.append(fa)
            arr = na

        return fr
