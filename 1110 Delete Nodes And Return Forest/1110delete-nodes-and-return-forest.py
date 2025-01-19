# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        r = []

        def check(n, p):
            k = n.val not in to_delete
            x = y = None
            if n.left:
                x = n.left
                if n.left.val in to_delete:
                    n.left = None
            if n.right:
                y = n.right
                if n.right.val in to_delete:
                    n.right = None
            if k and not p:
                r.append(n)
            if x:
                check(x, k)
            if y:
                check(y, k)
        
        check(root, False)
        return r
                    
            


            
        
        check(root, False)

        return r

