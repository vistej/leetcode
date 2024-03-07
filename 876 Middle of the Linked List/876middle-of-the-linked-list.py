# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 1
        hc = head
        while head.next:
            cnt = cnt + 1
            head = head.next
        centr = cnt // 2 + 1
        x = 1
        while hc.next:
            if x == centr:
                return hc
            x = x + 1
            hc = hc.next
        return head