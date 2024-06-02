# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        c = head
        l = 0
        while c:
            l += 1
            c = c.next
        m = l//2
        i = 0
        c = head
        while i < m - 1:
            c = c.next
            i += 1
        t = c.next
        c.next = t.next if t else None
        return head