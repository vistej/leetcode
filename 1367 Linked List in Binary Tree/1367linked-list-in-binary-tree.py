# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def check(tn, ln):
            if not ln.next:
                return True
            r = False
            if tn.left and tn.left.val == ln.next.val:
                r = r or check(tn.left, ln.next)
            if tn.right and tn.right.val == ln.next.val:
                r = r or check(tn.right, ln.next)
            return r
        
        def loo(n):
            r = False
            if n.val == head.val:
                r = check(n, head)
            if n.left:
                r = r or loo(n.left)
            if n.right:
                r = r or loo(n.right)
            return r
        
        return loo(root)