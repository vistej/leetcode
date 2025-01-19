# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r = head.next
        t = r
        n = t

        while n.next:
            n = n.next
            if n.val:
                t.val += n.val
            else:
                if n.next:
                    t.next = n
                    t = n
                else:
                    t.next = None
        return r