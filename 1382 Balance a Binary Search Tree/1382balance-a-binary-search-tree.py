# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def get_roots(root):
            if not root:
                return []
            return get_roots(root.left) + [root] + get_roots(root.right)
        
        def build(l, r, roots):
            if l > r:
                return None
            m = (l + r) // 2
            roots[m].left = build(l, m - 1, roots)
            roots[m].right = build(m + 1, r, roots)
            return roots[m]
        
        roots = get_roots(root)
        return build(0, len(roots) - 1, roots)