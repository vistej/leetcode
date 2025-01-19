# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ar = []
        hc = head
        while hc:
            ar.append(hc.val)
            hc = hc.next
        ar = sorted(ar)
        hc = head
        for a in ar:
            hc.val = a
            hc = hc.next
        return head