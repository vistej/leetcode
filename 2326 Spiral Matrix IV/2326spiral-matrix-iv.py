# Definition for singly-linaed list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ma = [[-1 for _ in range(n)] for _ in range(m)]
        x = 0
        y = 0
        while head and x <= m:
            a = y
            b = x
            while head and a < n:
                ma[b][a] = head.val
                head = head.next
                a += 1
            x += 1
            b = x
            a -= 1
            while head and b < m:
                ma[b][a] = head.val
                head = head.next
                b += 1
            n -= 1
            a -= 1
            b -= 1
            while head and a >= y:
                ma[b][a] = head.val
                head = head.next
                a -= 1
            m -= 1
            b -= 1
            a += 1
            while head and b >= x:
                ma[b][a] = head.val
                head = head.next
                b -= 1
            y += 1
            a = y
            b += 1



        return ma