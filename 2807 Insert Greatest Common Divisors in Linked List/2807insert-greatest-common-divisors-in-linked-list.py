# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        hc = head

        while hc.next:
            x = hc.next
            v = gcd(hc.val, x.val)

            hc.next = ListNode(v, x)
            hc = x
        
        return head